
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

csv_path = "data/raw/health_facilities.csv"
gpkg_path = "obio_akpor_analysis_ready.gpkg"

df = pd.read_csv(csv_path)

print("Columns:", df.columns.tolist())
print("\nFirst five records:")
print(df.head())

print("\nFacility types before cleaning:")
print(df["type"].value_counts(dropna=False))

df["type"] = df["type"].str.strip().replace({
    "PHC": "Primary Health Centre",
    "Primary Health Centre": "Primary Health Centre"
})

print("\nFacility types after cleaning:")
print(df["type"].value_counts(dropna=False))

df = df.dropna(subset=["latitude", "longitude"])

health_facilities = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(
        df["longitude"],
        df["latitude"]
    ),
    crs="EPSG:4326"
)

boundary = gpd.read_file(
    gpkg_path,
    layer=2
)

health_facilities = health_facilities.to_crs(boundary.crs)

output_path = "data/processed/my_health_facilities.gpkg"

health_facilities.to_file(
    output_path,
    layer="health_facilities",
    driver="GPKG"
)

print("\nNumber of facilities:", len(health_facilities))
print("\nGeometry types:")
print(health_facilities.geom_type.value_counts())
print("\nHealth facilities CRS:", health_facilities.crs)
print("Health facilities bounds:", health_facilities.total_bounds)

print("\nBoundary CRS:", boundary.crs)
print("Boundary bounds:", boundary.total_bounds)

fig, ax = plt.subplots(figsize=(10, 10))

boundary.plot(
    ax=ax,
    color="lightgrey",
    edgecolor="black",
    linewidth=0.8
)

health_facilities.plot(
    ax=ax,
    color="darkgreen",
    markersize=15,
    label="Health Facilities"
)

ax.set_title("Health Facilities in Obio-Akpor")
ax.legend()
ax.set_axis_off()

plt.tight_layout()

plt.savefig(
    "month-03/week-10/my_map.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nSaved to:", output_path)
print("Map saved to: month-03/week-10/my_map.png")
