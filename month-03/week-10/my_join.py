
import geopandas as gpd
import pandas as pd

gpkg_path = "obio_akpor_analysis_ready.gpkg"
csv_path = "streams_data.csv"

streams = gpd.read_file(gpkg_path, layer=6)
table = pd.read_csv(csv_path)

print("Spatial records:", len(streams))
print("CSV records:", len(table))

geometry_length = streams.geometry.length.round(3)
csv_length = table["length"].round(3)

print("Length verification:", geometry_length.equals(csv_length))

streams = streams.reset_index(drop=True)
table = table.reset_index(drop=True)

streams["stream_id"] = range(1, len(streams) + 1)
table["stream_id"] = range(1, len(table) + 1)

joined_before = streams.merge(
    table,
    on="stream_id",
    how="left",
    indicator=True
)

print("Matches before cleaning:", (joined_before["_merge"] == "both").sum())

clean_streams = streams.dropna(subset=["geometry"])
clean_table = table.dropna(subset=["length", "straight_m"])

joined_after = clean_streams.merge(
    clean_table,
    on="stream_id",
    how="left",
    indicator=True
)

print("Matches after cleaning:", (joined_after["_merge"] == "both").sum())

joined_after = joined_after.drop(columns="_merge")

output_path = "data/processed/my_streams_joined.gpkg"

joined_after.to_file(
    output_path,
    layer="my_streams_joined",
    driver="GPKG"
)

print("Joined dataset saved to:", output_path)
