
import geopandas as gpd

gpkg_path = "obio_akpor_analysis_ready.gpkg"

print(gpd.list_layers(gpkg_path))

roads = gpd.read_file(
    gpkg_path,
    layer=4
)

print(roads.head())
print("Rows and columns:", roads.shape)
print(roads.geom_type.value_counts())
print("CRS:", roads.crs)
print("Bounds:", roads.total_bounds)
