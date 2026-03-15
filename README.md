# FCPD Crime Records Analyzer

Python OOP application that processes and queries Fairfax County Police Department crime report data using custom container classes.

## Overview

This project reads weekly crime report data from the Fairfax County Police Department and provides tools to search, filter, and generate statistics from the dataset. It was built to demonstrate Python OOP concepts including inheritance, container classes, and data abstraction.

## How to Run

1. Clone the repo:
```bash
git clone https://github.com/eliashafiz1/fcpd-crime-analyzer.git
cd fcpd-crime-analyzer
```

2. Run the program (Python 3 required, no external packages needed):
```bash
python fcpd_crime_analyzer.py
```

The `CrimeReports.csv` dataset is included in the repo, so it works out of the box.

## What It Does

- **Loads** 1,000+ crime incident records from CSV into structured Python objects
- **Filters** records by offense type, zip code, or locale
- **Counts** crimes by type or zip code, sorted by frequency with percentage breakdowns
- **Returns** filtered subsets for further analysis (e.g. all incidents in zip 22030)

## Example Usage

```python
FC = FCPDCrime("Fairfax Police Calls")
FC.load('CrimeReports.csv')

FC.printCrimes()                                  # all records
FC.printCrimes(searchKey='assault')               # filter by offense
FC.printCrimes(zip='22030')                       # filter by zip code
FC.printCrimes(searchKey='assault', zip='22030')  # combine filters

FC.countByZip()                                   # crime counts by zip
FC.countByCrime('all')                            # crime counts by type
FC.countByCrime('22030')                          # crime counts for a specific zip

ZL = FC.zipCodeList(zip='22030')                  # get list for a zip code
for c in ZL:
    print(c)
```

## Key Concepts Demonstrated

- **Inheritance**: `FCPDCrime` extends Python's built-in `list` class
- **Data abstraction**: raw CSV rows are managed through structured methods
- **Container class pattern**: custom methods for search, filter, and aggregation over a collection of records
- **Selection sort**: results sorted by frequency using a manual sorting algorithm

## Dataset

The included `CrimeReports.csv` contains weekly crime call data downloaded from the [Fairfax County Police Download Center](https://www.fairfaxcounty.gov/police/chief/crime-reports). Each record includes fields for offense code, description, date, time, address, city, state, and zip code.

## Built With

- Python 3
- No external dependencies (uses only the built-in `csv` module)
