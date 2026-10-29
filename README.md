# GeoDev Lab Project

A practical GIS and Python project documenting my learning and development through GeoDev Lab Africa.

The project began with a GIS investigation of flood exposure and progressed into Python programming, development environment setup, data handling, and reusable functions for analysing CSV datasets.

## Research Question

Which areas of the study area are most exposed to flooding in relation to drainage conditions, elevation, and surface-water patterns?

---

## Weekly Progress Log

### Week 1 — Project Brief

Defined the project question, objectives, datasets, data sources, and proposed GIS outputs.

**Deliverable:** [`project-brief.md`](project-brief.md)

### Week 2 — Data Notes

Documented relevant project data, data sources, and supporting information for the GIS investigation.

**Deliverable:** [`data-notes.md`](data-notes.md)

### Week 3 — Spatial Analysis

Conducted the initial spatial analysis for the study area and documented the findings.

**Deliverable:** [`obio_akpor_analysis_ready.gpkg`](obio_akpor_analysis_ready.gpkg) and the associated analysis file, where applicable.

### Week 4 — River Buffer Mapping

Created a river buffer map to examine proximity to surface water and its relevance to flood exposure.

The Week 4 analysis identified the mapped river corridor and its 100 m buffer as an area of proximity to surface water. Further analysis is needed to incorporate elevation, drainage conditions, and broader surface-water patterns into the flooding exposure assessment.

**Deliverable:** [Week 4 river buffer map](week4_river_buffer_map.png) and associated project files.

### Week 5 — Python Development Environment

Set up and verified the Python development environment in Visual Studio Code. Created and ran a simple Python script to confirm that Python was working.

**Deliverable:** [`hello.py`](hello.py)

### Week 6 — Python Project Setup with uv

Configured the Python project using `uv` and established the project environment. Used `check.py` to practise checking the installed pandas version.

**Deliverables:** [`pyproject.toml`](pyproject.toml), [`uv.lock`](uv.lock), and [`check.py`](check.py)

### Week 7 — Python CSV Analysis

Developed `analyse.py` to read ward data from `wards.csv`, extract area values, convert square kilometres to hectares, and classify wards as large or small using an area threshold of 9 km².

**Deliverables:** [`analyse.py`](analyse.py) and [`wards.csv`](wards.csv)

### Week 8 — CSV Data Inspection

Week 8: `inspect_data.py` summarises length and straight-line distance (`straight_m`) in my Obio/Akpor streams data.

**Deliverables:** [`inspect_data.py`](inspect_data.py), [`streams_data.csv`](streams_data.csv), and [`screenshots/week8.png`](screenshots/week8.png)



### Week 9 – Consolidation and Refactoring

Week 9: `summary.py` refactors the Week 8 data inspection script into three reusable functions: `read_rows()`, `clean_values()`, and `summarise()`. The `summarise_all()` function calculates descriptive statistics for the `length` and `straight_m` columns in my Month 1 dataset.

**Deliverables:** [`summary.py`](summary.py) and [`screenshots/week9.png`](screenshots/week9.png).

### Month 2 reflection

This month, I gained a better understanding of how Python functions, loops, dictionaries, and CSV files work together to process data. The idea that finally clicked for me was breaking a long script into smaller functions, with each function performing one specific task. I still need more practice handling errors and working confidently with different data structures. My capstone shows that my Month 1 stream dataset contains 60 records and allows me to summarise the length and straight-line distance columns using descriptive statistics.


## Repository Organisation

Project files are maintained directly in the repository root rather than in separate nested folders for each week.

The [`screenshots/`](screenshots) directory contains visual evidence of weekly practical work.

## Screenshots

- [`screenshots/week5.png`](screenshots/week5.png): Week 5 practical
- [`screenshots/week6.png`](screenshots/week6.png): Week 6 practical
- [`screenshots/week7.png`](screenshots/week7.png): Week 7 practical
- [`screenshots/week8.png`](screenshots/week8.png): Week 8 practical