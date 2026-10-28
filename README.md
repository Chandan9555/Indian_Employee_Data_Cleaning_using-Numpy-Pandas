# Indian Employee Dataset Cleaning Using Python

## Project Title
**Indian Employee Dataset Cleaning and Preprocessing**

## Short Description / Purpose
This project demonstrates how to clean and preprocess an Indian employee dataset using Python. It uses Pandas and NumPy to inspect missing values, handle missing numeric values, remove duplicate records, replace negative salary values, identify salary outliers using the three-standard-deviation rule, and export a cleaned CSV file.

The goal is to prepare employee data for further analysis and reporting.

## Tech Stack
- **Python**
- **Pandas** — loading, inspecting, and transforming tabular data
- **NumPy** — numerical operations and conditional replacements
- **CSV** — input and output data format

## Data Source
This repository uses the following CSV files:

- `indian_employee_dataset.csv` — original employee dataset used as input.
- `cleaned_indian_employee_Data.csv` — output file intended to contain the cleaned dataset.

The data files are included with this project. Check the dataset columns and contents before using the data for any business or research conclusions.

## Features / Highlights
- Loads the original CSV dataset with Pandas.
- Displays the first rows of the dataset.
- Checks missing values in each column.
- Attempts to fill missing salary values with the mean and missing performance ratings with the median.
- Attempts to replace infinite values and fill remaining numeric missing values.
- Removes duplicate rows.
- Replaces negative salary values with the average salary.
- Filters salary values outside the mean ± 3 standard deviations.
- Exports the result to a CSV file without the DataFrame index.

## Project Structure

```text
Indian-Employee-Dataset-Cleaning/
├── indian_employee_dataset.csv
├── cleaned_indian_employee_Data.csv
├── data_clean.py
└── README.md
```

## Requirements
- Python 3
- Pandas
- NumPy

## Learning Outcomes
- Working with CSV files in Python
- Inspecting missing values with Pandas
- Using mean and median for numeric missing-value imputation
- Removing duplicate records
- Applying NumPy conditional logic
- Detecting salary outliers using standard deviation
- Exporting processed data for further analysis

## Future Improvements
- Add before-and-after data quality summaries.
- Validate column data types and required fields.
- Document how many missing values, duplicates, negative salaries, and outliers are handled.
- Add automated checks to verify the cleaned output.
- Add visualizations to explore employee salary and performance distributions.

