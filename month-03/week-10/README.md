# Week 10: GeoPandas, layers as tables

## What this folder contains

- `explore_pandas.py`: first look at the ward population table using pandas.
- `filter_sort.py`: filters, sorts and analyses ward population records.
- `explore_layer.py`: loads and inspects the wards GeoPackage layer.
- `geom_props.py`: examines polygon geometry properties, validity and centroid.
- `csv_to_points.py`: converts health facility coordinates from CSV into point geometries.
- `join_population.py`: joins population data to ward polygons after cleaning names.
- `make_map.py`: creates a map showing health facilities within ward boundaries.
- `save_outputs.py`: exports the processed geospatial outputs.
- `facilities_map.png`: generated map of health facilities in Ibadan North.
- `wards_table.csv`: exported ward attribute table.

## How to run it

From the repository root:

```bash
uv run month-03/week-10/join_population.py
```

## What I found

The ward population dataset contained 12 wards and recorded a total population of 385,800. The wards layer contained 12 polygon features and used EPSG:4326. I converted 41 health facility records from CSV coordinates into point geometries and successfully mapped them over the ward boundaries. The initial population join matched 9 of the 12 wards on the first attempt.

## What went wrong and how I fixed it

The initial map displayed ward boundaries without the health facility locations because the facilities layer had been loaded but not plotted. I corrected the mapping script by plotting the facilities layer over the ward polygons, making the health facility points visible in the final map. The initial population join also reported 9 matches out of 12, highlighting the need to examine unmatched ward names.