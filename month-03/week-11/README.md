# Week 11: Stream Network Spatial Analysis

## Project Overview

This practical applies spatial analysis techniques using GeoPandas to examine a stream network. The project uses stream line features, stream points and stream buffer polygons to perform coordinate reference system (CRS) transformation, length calculation, spatial counting, nearest-distance analysis and geometry validation.

All analyses were conducted using the stream dataset.

## 1. Coordinate Reference System and Stream Length (`my_crs.py`)

The original stream dataset uses **EPSG:32632**. The `estimate_utm_crs()` method was used to identify a suitable projected coordinate reference system.

The dataset was reprojected to EPSG:32632, and the length of each stream feature was calculated in kilometres.

The calculated total stream length was approximately **44.8 km**.

A projected CRS was used because measurements calculated directly from geographic coordinates may be inaccurate.

## 2. Spatial Join and Point Counting (`my_count.py`)

The `sjoin()` method was used to identify stream points falling within stream buffer polygons.

The resulting spatial join was grouped using `groupby()` to calculate the number of points associated with each buffer polygon.

The counts were subsequently merged back into the buffer polygon dataset to ensure that every polygon retained a count, including polygons with zero points.

The total-counted check was printed to verify the spatial join results.

## 3. Nearest Stream Distance (`my_reach.py`)

The `sjoin_nearest()` method was used to identify the nearest other stream feature.

The distance between stream features was calculated in metres and converted into kilometres.

The analysis produced an average nearest-stream distance of approximately **0.054 km (54 metres)**.

This method was selected to examine the spatial proximity of stream features within the study area.

## 4. Geometry Validation (`my_validity.py`)

Geometry validation was performed on the stream buffer polygon layer using GeoPandas.

The `is_valid` property was used to identify invalid geometries, while `make_valid()` was applied as the correction method.

The analysis identified:

- Invalid geometries before correction: 0
- Invalid geometries after correction: 0

This indicates that the examined buffer geometries were already valid and did not require correction.

## 5. Output Files

The generated results were saved in the following locations:

- `data/processed/my_nearest_stream_results.gpkg`
- `month-03/week-11/my_reach_map.png`

## 6. Limitations of the Analysis

The nearest-distance analysis measures the geometric distance between stream features rather than the actual distance water travels through the stream network. It does not account for water flow direction, elevation, stream connectivity or hydrological conditions. Additionally, overlapping stream buffers may cause the same point to be counted in multiple polygons. Therefore, the results should be interpreted as spatial proximity and point distribution measurements rather than direct measurements of hydrological connectivity or water movement.