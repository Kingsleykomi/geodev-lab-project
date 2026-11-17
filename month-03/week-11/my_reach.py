
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load stream dataset
streams = gpd.read_file(
    "data/processed/my_streams_joined.gpkg",
    layer="my_streams_joined"
)

print("Original CRS:", streams.crs)
print("Total stream features:", len(streams))

# 2. Estimate the appropriate UTM CRS
utm_crs = streams.estimate_utm_crs()

print("Suggested UTM CRS:", utm_crs)

# 3. Reproject streams
streams = streams.to_crs(utm_crs)

# 4. Create a unique ID for every stream feature
streams = streams.reset_index(drop=True)
streams["stream_id"] = streams.index

# 5. Find the nearest OTHER stream feature
results = []

for i in range(len(streams)):

    source = gpd.GeoDataFrame(
        {
            "stream_id": [i],
            "geometry": [streams.geometry.iloc[i]]
        },
        crs=streams.crs
    )

    # Exclude the current stream from the candidates
    candidates = streams.drop(index=i)

    candidates = candidates[["stream_id", "geometry"]]

    if candidates.empty:
        continue

    nearest = gpd.sjoin_nearest(
        source,
        candidates,
        how="left",
        distance_col="distance_m",
        lsuffix="source",
        rsuffix="nearest"
    )

    for _, row in nearest.iterrows():
        results.append({
            "stream_id": row["stream_id_source"],
            "nearest_stream_id": row["stream_id_nearest"],
            "distance_m": row["distance_m"]
        })

# 6. Convert results into a DataFrame
distance_results = pd.DataFrame(results)

# 7. Convert metres to kilometres
distance_results["distance_km"] = (
    distance_results["distance_m"] / 1000
).round(3)

# 8. Display results
print("\nNearest stream distances:")
print(distance_results.head(10))

# 9. Calculate average distance
print(
    "\nAverage distance to nearest other stream:",
    round(distance_results["distance_km"].mean(), 3),
    "km"
)

# 10. Attach results to stream geometries
nearest_streams = streams.merge(
    distance_results,
    on="stream_id",
    how="left"
)

# 11. Save result layer
output_path = (
    "data/processed/my_nearest_stream_results.gpkg"
)

nearest_streams.to_file(
    output_path,
    layer="nearest_stream_results",
    driver="GPKG"
)

print("\nResult saved to:", output_path)

# 12. Create stream map
fig, ax = plt.subplots(figsize=(10, 8))

nearest_streams.plot(
    column="distance_km",
    cmap="viridis",
    legend=True,
    linewidth=1.2,
    ax=ax,
    legend_kwds={
        "label": "Distance to nearest other stream (km)"
    }
)

ax.set_title("Nearest Stream Feature Analysis")
ax.set_axis_off()

# 13. Save map
plt.savefig(
    "month-03/week-11/my_reach_map.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Map saved successfully.")
