# Data notes

## Obio/Akpor LGA boundary
- Source: GRID3 Nigeria
- 1 feature, polygon
- Column: lganame (text), with value Obio/Akpor
- No null observed in lganame
- Covers the study area

## OSM roads, extracted via QuickOSM
- Query: highway=* within Obio/Akpor boundary
- 24,973 features, lines
- Some attributes contain NULL values
- Coverage is extensive across the study area

## OSM drainage network
- Query: waterway=drain within Obio/Akpor boundary
- 1 feature, line
- No null observed in the waterway field
- Coverage is limited, so not all drainage channels may be mapped

## OSM ditches
- Query: waterway=ditch within Obio/Akpor boundary
- 8 features, lines
- Some attributes contain NULL values
- Coverage is limited

## OSM rivers
- Query: waterway=river within Obio/Akpor boundary
- 31 features, lines
- Some attributes contain NULL values
- Includes mapped rivers and named waterways

## OSM streams
- Query: waterway=stream within Obio/Akpor boundary
- 101 features, lines
- Some attributes contain NULL values
- Coverage includes mapped streams in the study area

## GRID3 settlement extents
- Source: GRID3 Nigeria
- 1,106 features, polygons
- Includes settlement and building-related attributes
- Some attributes may contain NULL values
- Clipped to the Obio/Akpor study area

## Copernicus GLO-30 elevation
- Source: OpenTopography / Copernicus GLO-30
- 30-metre raster
- Elevation/surface values are represented as raster cells
- Clipped to the Obio/Akpor study area
- Used to examine elevation and terrain characteristics

## Coverage notes
- OSM data is crowdsourced, so mapped features may not represent every road, drainage channel, river, or stream.
- The settlement layer was clipped to Obio/Akpor so that it matches the study area.
- The GLO-30 elevation layer was clipped to the study area.
