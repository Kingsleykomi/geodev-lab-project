# GeoDev Lab Project

A practical GIS and Python project documenting my learning and development through GeoDev Lab Africa.

The project began with a GIS investigation of flood exposure and progressed into Python programming, development environment setup, data handling, and reusable functions for analysing CSV datasets.

## Research Question

Which areas of the study area are most exposed to flooding in relation to drainage conditions, elevation, and surface-water patterns?

---

# Month 1 — GIS and Spatial Analysis

Month 1 focused on defining the GIS project, documenting and preparing spatial datasets, and conducting an initial spatial analysis.

## Week 1 — Project Brief

Defined the project question, objectives, datasets, data sources, and proposed GIS outputs.

**Deliverable:**
- [Project Brief](Month%201/Week-1/project-brief.md)

## Week 2 — Data Notes

Documented the downloaded datasets, their sources, important attribute fields, geometry, and data limitations.

**Deliverable:**
- [Data Notes](Month%201/week-2/data-notes.md)

## Week 3 — Prepared Data

Prepared the spatial data using the projected working coordinate reference system (CRS), clipped the datasets to the study area, and saved the prepared data as an analysis-ready GeoPackage.

**Deliverable:**
- [Analysis-ready GeoPackage](Month%201/week-3/obio_akpor_analysis_ready.gpkg)

## Week 4 — Spatial Analysis

Created a 100 m buffer around the mapped river feature using the projected CRS. The output contained one feature, and no empty geometry was found.

**Deliverable:**
- [Week 4 River Buffer Map](Month%201/week-4/week4_river_buffer_map.png)

### Month 1 Result

The initial analysis identified the mapped river corridor and its 100 m buffer as an area of proximity to surface water. Further analysis is required to incorporate elevation, drainage conditions, and broader surface-water patterns into the flood-exposure assessment.

**Month 1 Summary:**
- [Read the Month 1 Summary](month-1-summary.md)

---

# Month 2 — Development Environment and Early Python

Month 2 focused on Python development, project environment management, programming fundamentals, CSV data inspection, and reusable functions.

## Week 5 — Python Development Environment

Set up and verified the Python development environment in Visual Studio Code. Tested Python by checking the installed version, inspecting the working directory, and running a basic Python script.

**Deliverable:**
- [hello.py](Month%202/week-5/hello.py)

**Screenshot:**
- [Week 5 Screenshot](screenshots/week5.png)

## Week 6 — Python Project Setup with uv

Configured the Python project using `uv`, established the project dependency configuration, and added pandas for data analysis. The environment was prepared for subsequent Python practicals.

**Deliverables:**
- [pyproject.toml](Month%202/week-6/pyproject.toml)
- [uv.lock](Month%202/week-6/uv.lock)

**Screenshot:**
- [Week 6 Screenshot](screenshots/week6.png)

## Week 7 — Python: The Six Ideas

Worked with Python to read CSV files, process rows, convert area values into numeric data, calculate area in hectares, and classify wards according to their area. Also used a separate script to verify the pandas installation.

**Deliverables:**
- [analyse.py](Month%202/week-7/analyse.py)
- [check.py](Month%202/week-7/check.py)
- [wards.csv](Month%202/week-7/wards.csv)

**Screenshot:**
- [Week 7 Screenshot](screenshots/week7.png)

## Week 8 — CSV Data Inspection and Reusable Functions

Developed `inspect_data.py` to inspect CSV datasets using Python. The practical covers reading CSV data, handling empty values, working with dictionaries, and using a reusable function to return summary statistics for numeric columns.

The function is designed to report the smallest value, largest value, and count of valid numeric values for a selected column. The practical uses the Week 8 CSV dataset to test the inspection of two numeric columns.

**Deliverables:**
- [inspect_data.py](Month%202/week-8/inspect_data.py)
- [Week 8 CSV Dataset](Month%202/week-8/ward.csv)

**Screenshot:**
- [Week 8 Screenshot](screenshots/week8.png)

---

## Screenshots

Screenshots documenting the Month 2 practicals are available in the `screenshots/` folder.

- [Week 5 — Python Environment](screenshots/week5.png)
- [Week 6 — Project Setup](screenshots/week6.png)
- [Week 7 — Python Fundamentals](screenshots/week7.png)
- [Week 8 — CSV Inspection](screenshots/week8.png)

---

## Repository Structure

The repository is organised by month and week to make each practical and its deliverables easy to locate.

- `Month 1/` — Weeks 1–4: GIS project planning, data documentation, spatial data preparation, and spatial analysis.
- `Month 2/` — Weeks 5–8: Python environment setup, project configuration, Python fundamentals, and CSV data inspection.
- `screenshots/` — Screenshots documenting the weekly practicals.
- `month-1-summary.md` — Summary of the first month's GIS work.
- `README.md` — Project overview, weekly progress, and links to deliverables.
