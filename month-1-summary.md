# Month 1 Summary

## Question

Which areas of Obio/Akpor Local Government Area are most exposed to flooding in relation to drainage conditions, elevation, and surface-water patterns?

## Operation

I ran a 100 m river buffer on the Obio/Akpor river data. I chose a buffer because the question asks about areas within a specified distance of surface water, and the Week 4 practical identifies buffer as the appropriate operation for questions such as areas within 100 metres of a river.

## Expected

I expected the buffer to create a zone extending 100 metres around the mapped river feature, with the output saved as a GeoPackage in the projected CRS.

## What I got

The 100 m river buffer was created successfully as a GeoPackage in the projected CRS (EPSG:32632 — WGS 84 / UTM zone 32N). The output contained 1 feature. The result was checked on the map, the attribute table, by manually checking one feature, and for empty geometry. No empty geometry was found.

## What surprised me

The buffer output contained one feature, representing the buffered river geometry, rather than multiple separate buffer features.

## What data I still need

I still need to incorporate elevation, drainage conditions, and surface-water patterns into the analysis so that the flooding exposure question can be examined beyond proximity to rivers alone.