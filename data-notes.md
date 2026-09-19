# Data notes

## Obio/Akpor LGA boundary

- Source: GRID3 Nigeria — https://grid3.org/geospatial-data-nigeria
- Feature count: 1
- Key columns: lganame
- Geometry: Polygon
- Gaps/missing values: No NULL observed in lganame; the selected polygon covers the study area.

## OSM roads, extracted via QuickOSM

- Source: OpenStreetMap — https://www.openstreetmap.org/
- Query: highway=* within Obio/Akpor boundary
- Feature count: 24,973
- Key columns: highway, name, lanes:forward, lanes:both_ways
- Geometry: Line
- Gaps/missing values: Some attributes contain NULL values; road coverage is extensive across the study area.

## OSM drainage network

- Source: OpenStreetMap — https://www.openstreetmap.org/
- Query: waterway=drain within Obio/Akpor boundary
- Feature count: 1
- Key columns: waterway, full_id, osm_id, osm_type
- Geometry: Line
- Gaps/missing values: No NULL observed in the waterway field; coverage is limited, so not all drainage channels may be mapped.

## OSM ditches

- Source: OpenStreetMap — https://www.openstreetmap.org/
- Query: waterway=ditch within Obio/Akpor boundary
- Feature count: 8
- Key columns: waterway, full_id, osm_id, osm_type
- Geometry: Line
- Gaps/missing values: Some attributes contain NULL values; coverage is limited.

## OSM rivers

- Source: OpenStreetMap — https://www.openstreetmap.org/
- Query: waterway=river within Obio/Akpor boundary
- Feature count: 31
- Key columns: waterway, name, full_id, osm_id, osm_type
- Geometry: Line
- Gaps/missing values: Some name attributes are NULL; not every river or watercourse may be mapped.

## OSM streams

- Source: OpenStreetMap — https://www.openstreetmap.org/
- Query: waterway=stream within Obio/Akpor boundary
- Feature count: 101
- Key columns: waterway, name, full_id, osm_id, osm_type
- Geometry: Line
- Gaps/missing values: Some name attributes are NULL; coverage depends on OpenStreetMap mapping.

## GRID3 settlement extents

- Source: GRID3 Nigeria — https://grid3.org/geospatial-data-nigeria
- Feature count: 11,066
- Key columns: block_id, country, iso3, block_area_sqm, block_perimeter, building_count
- Geometry: Polygon
- Gaps/missing values: Settlement blocks contain attribute fields with available and NULL values; the dataset was clipped to the Obio/Akpor study area.

## Copernicus GLO-30 elevation

- Source: OpenTopography / Copernicus GLO-30 — https://portal.opentopography.org/datasetMetadata.jsp?otCollectionID=OT.032021.4326.1
- Feature count: Not applicable; this is a raster dataset containing one elevation layer.
- Key columns: Band 1 (elevation values)
- Geometry: Raster grid
- Gaps/missing values: No missing-value issue was observed when the raster was opened in QGIS; the dataset was clipped to the Obio/Akpor study area.
 ## CRS and preparation

- Source layers used for the project were in EPSG:4326 (WGS 84).
- Study area: Obio/Akpor Local Government Area, Rivers State.
- The study-area boundary was extracted and saved as `study_area.gpkg`.
- Project layers were clipped to the Obio/Akpor study area.
- Clipped layers were reprojected to EPSG:32632 (WGS 84 / UTM Zone 32N).
- Working files are saved in `data/processed/`.
- Files in `data/raw/` were left untouched.
