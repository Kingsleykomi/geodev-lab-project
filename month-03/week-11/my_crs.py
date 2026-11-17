
import geopandas as gpd

# Read stream dataset
streams = gpd.read_file(
    "data/processed/my_streams_joined.gpkg",
    layer="my_streams_joined"
)

print("CRS:", streams.crs)

# Calculate length before reprojection (wrong)
streams["length_wrong"] = streams.length

print(streams[["length_wrong"]].head(3))

# Estimate suitable UTM CRS
print("Suggested UTM:", streams.estimate_utm_crs())

# Reproject streams to the suggested UTM CRS
streams_utm = streams.to_crs(
    streams.estimate_utm_crs()
)

# Calculate length in kilometres
streams_utm["length_km"] = (
    streams_utm.length / 1000
)

print(streams_utm[["length_km"]].head(3))

# Calculate total stream length
print(
    "Total stream length:",
    round(streams_utm["length_km"].sum(), 1),
    "km"
)
