# Week 10: GeoPandas, layers as tables

## What this folder contains

### Guided scripts

- `explore_pandas.py`: explores the ward population dataset using pandas.
- `filter_sort.py`: filters, sorts and analyses ward population records.
- `explore_layer.py`: loads and inspects the wards GeoPackage layer.
- `geom_props.py`: examines polygon geometry properties, validity and centroids.
- `csv_to_points.py`: converts health facility coordinates from CSV into point geometries.
- `join_population.py`: joins population data to ward polygons.
- `make_map.py`: creates a map showing health facilities within ward boundaries.
- `save_outputs.py`: exports processed geospatial outputs.

### Generated outputs

- `facilities_map.png`: generated map of health facilities.
- `wards_table.csv`: exported ward attribute table.

### Independent challenge files

- `my_explore.py`: explores my Obio-Akpor spatial dataset and reports layer information, feature counts, geometry types, CRS and bounds.
- `my_points.py`: converts the teaching health facilities CSV into a point layer, cleans facility type values and generates a map.
- `my_join.py`: joins stream attribute data to the stream spatial layer and saves the joined dataset.
- `my_map.png`: generated map from my independent mapping exercise.

## How to run the scripts

Run commands from the repository root using the project environment.

```bash
uv run month-03/week-10/my_explore.py
uv run month-03/week-10/my_points.py
uv run month-03/week-10/my_join.py
```

## What I found

My spatial exploration identified the stream layer and its associated spatial properties within the Obio-Akpor dataset.

The stream attribute table contained 60 records, matching the 60 spatial stream features. I verified that the geometry lengths and CSV length values matched.

For the independent point exercise, I used the teaching `health_facilities.csv` dataset because my own CSV contained stream measurements rather than point coordinates.

The facility type column initially contained separate labels for `PHC` and `Primary Health Centre`. After cleaning, both were standardised as `Primary Health Centre`.

The cleaned dataset contained 41 health facility point features and was saved as `data/processed/my_health_facilities.gpkg`.

## What I learned

This exercise strengthened my understanding of using GeoPandas to explore vector datasets, inspect spatial properties, convert tabular coordinate data into point geometries, clean attribute values and join tabular data to spatial layers.

I also gained practical experience verifying attribute-to-geometry matches and examining coordinate reference systems and spatial extents before mapping.

## Outputs

Processed outputs are saved in `data/processed/`, while scripts and the generated map are stored in `month-03/week-10/`.

