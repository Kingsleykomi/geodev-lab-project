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
- Clipped layers were reprojected to EPSG:32632 (WGS 84 / UTM Zone 32N) because it is the appropriate projected CRS for the study area and allows distances and areas to be measured in metres.
- The analysis-ready GeoPackage is saved as `data/processed/obio_akpor_analysis_ready.gpkg`.
- Files in `data/raw/` were left untouched.
  ## Five data quality checks

### 1. Completeness
The data was checked against the Google Satellite basemap and the study area. The main layers are present for the Obio/Akpor study area, but OpenStreetMap drainage data has gaps. In particular, the mapped drains and ditches do not represent all drainage features visible on the satellite imagery. These gaps were flagged rather than treated as complete coverage.

### 2. Currency
The datasets were reviewed for available source information and dates. The OSM data represents mapped features available from OpenStreetMap at the time of download, while the other datasets have their own source dates. The source dates should be considered when interpreting the results, particularly for features that may have changed over time.

### 3. Positional accuracy
The vector layers were visually compared with the Google Satellite basemap. The mapped features generally fall in the expected locations, although satellite imagery and mapped features may not align perfectly in every location. No major positional problem was identified that required correction.

### 4. Attribute accuracy
The attribute information was reviewed for the downloaded layers. The main feature classifications and attributes are usable for the intended analysis, but OpenStreetMap attributes depend on how features were mapped and tagged. No major attribute problem requiring correction was identified; limitations in OSM attributes were flagged.

### 5. Fitness for purpose
The prepared data is suitable for the planned flooding analysis because it provides the Obio/Akpor boundary, roads, drainage-related features, rivers, streams, settlements, and elevation data. However, the incomplete OSM drainage coverage means the absence of a mapped drainage feature should not be interpreted as proof that no drainage exists.
