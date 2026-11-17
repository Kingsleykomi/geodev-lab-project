
import geopandas as gpd

# Load stream dataset
streams = gpd.read_file(
    "data/processed/my_streams_joined.gpkg",
    layer="my_streams_joined"
)

# Reproject to suitable UTM CRS
streams = streams.to_crs(streams.estimate_utm_crs())

# Create buffer polygons around streams
buffers = streams.copy()
buffers["geometry"] = buffers.geometry.buffer(100)

print("Geometry type:", buffers.geom_type.unique())

# Count invalid geometries before correction
invalid_before = (~buffers.is_valid).sum()

print("Invalid before:", invalid_before)

# Fix invalid geometries
buffers["geometry"] = buffers.geometry.make_valid()

# Count invalid geometries after correction
invalid_after = (~buffers.is_valid).sum()

print("Invalid after:", invalid_after)

# Print validity confirmation
print("Valid now:", buffers.is_valid.all())
print("New geometry types:", buffers.geom_type.unique())
