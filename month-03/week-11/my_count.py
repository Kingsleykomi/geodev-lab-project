
import geopandas as gpd

# 1. Load stream datasets
streams = gpd.read_file(
    "data/processed/my_streams_joined.gpkg",
    layer="my_streams_joined"
)

points = gpd.read_file(
    "data/processed/my_stream_points.gpkg",
    layer="stream_points"
)

# 2. Reproject both datasets to a suitable UTM CRS
utm_crs = streams.estimate_utm_crs()

streams = streams.to_crs(utm_crs)
points = points.to_crs(utm_crs)

print("Working CRS:", utm_crs)

# 3. Create buffer polygons around streams
buffers = streams[["geometry"]].copy()

buffers["buffer_id"] = range(len(buffers))

buffers["geometry"] = buffers.geometry.buffer(100)

# 4. Spatial join: points within stream buffers
joined = gpd.sjoin(
    points,
    buffers[["buffer_id", "geometry"]],
    how="inner",
    predicate="within"
)

# 5. Count points in each buffer
counts = (
    joined.groupby("buffer_id")
    .size()
    .reset_index(name="point_count")
)

# 6. Merge counts back to all buffer polygons
result = buffers.merge(
    counts,
    on="buffer_id",
    how="left"
)

# Include buffers with zero points
result["point_count"] = (
    result["point_count"].fillna(0).astype(int)
)

# 7. Print results
print("\nStream buffer point counts:")
print(result[["buffer_id", "point_count"]].head(10))

# 8. Total-counted check
print("\nTotal points counted:", result["point_count"].sum())
print("Points in spatial join:", len(joined))
print("Original stream points:", len(points))
