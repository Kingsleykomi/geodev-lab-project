# GeoDev Lab Project

A practical GIS and Python project documenting my learning and development through GeoDev Lab Africa.

The project began with a GIS investigation of flood exposure and progressed into Python programming, development environment setup, data handling, and reusable functions for analysing CSV datasets.

## Research Question

Which areas of the study area are most exposed to flooding in relation to drainage conditions, elevation, and surface-water patterns?

---

## Weekly Progress Log

### Week 1 — Project Brief

Defined the project question, objectives, datasets, data sources, and proposed GIS outputs.

**Deliverable:** `project-brief.md`

### Week 2 — Data Notes

Documented relevant project data, data sources, and supporting information for the GIS investigation.

**Deliverable:** `data-notes.md`

### Week 3 — Spatial Analysis

Conducted the initial spatial analysis for the study area and documented the findings.

**Deliverable:** `obio_akpor_analysis_ready.gpkg` and the associated analysis file, where applicable.

### Week 4 — River Buffer Mapping

Created a river buffer map to examine proximity to surface water and its relevance to flood exposure.

The Week 4 analysis identified the mapped river corridor and its 100 m buffer as an area of proximity to surface water. Further analysis is needed to incorporate elevation, drainage conditions, and broader surface-water patterns into the flooding exposure assessment.

**Deliverable:** Week 4 river buffer map and associated project files.

### Week 5 — Python Development Environment

Set up and verified the Python development environment in Visual Studio Code. Created and ran a simple Python script to confirm that Python was working.

**Deliverable:** `hello.py`

### Week 6 — Python Project Setup with uv

Configured the Python project using `uv` and established the project environment. Used `check.py` to practise checking the installed pandas version.

**Deliverables:** `pyproject.toml`, `uv.lock`, and `check.py`

### Week 7 — Python CSV Analysis

Developed `analyse.py` to read ward data from `wards.csv`, extract area values, convert square kilometres to hectares, and classify wards as large or small using an area threshold of 9 km².

**Deliverables:** `analyse.py` and `wards.csv`

### Week 8 — CSV Data Inspection

- Week 8: `inspect_data.py` summarises two columns in my project dataset using Python.

**Deliverables:** `inspect_data.py`, the appropriate project CSV, and `screenshots/week8.png`

---

## Repository Organisation

Project files are maintained directly in the repository root rather than in separate nested folders for each week.

The `screenshots/` directory contains visual evidence of weekly practical work.

## Screenshots

- `screenshots/week5.png` — Week 5 practical
- `screenshots/week6.png` — Week 6 practical
- `screenshots/week7.png` — Week 7 practical
- `screenshots/week8.png` — Week 8 practical 
