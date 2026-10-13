# Day-7: Student Performance Analysis

## Project Overview

This project analyzes student academic performance using Python.
It uses a real dataset from the UCI Machine Learning Repository
and applies data cleaning, analysis, statistics, and visualization.

## Objectives

- Load and explore a real CSV dataset.
- Check for missing values and duplicate records.
- Calculate students' average grades.
- Categorize student performance.
- Analyze weekly study-time categories and final grades.
- Create visualizations and generate key insights.

## Dataset

**Dataset Name:** Student Performance  
**Source:** UCI Machine Learning Repository  
**URL:** https://archive.ics.uci.edu/dataset/320/student%2Bperformance

The project uses `student-mat.csv`, which contains student information
and mathematics grades from Portuguese secondary schools.

Important columns:

- `studytime`: Weekly study-time category.
- `absences`: Number of school absences.
- `G1`: First-period grade.
- `G2`: Second-period grade.
- `G3`: Final grade.

Grades are generally on a scale from 0 to 20.
The study-time column uses categories rather than exact hours.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code

## Data Analysis

- Inspected the dataset using `head()`, `shape`, `info()`, and `describe()`.
- Checked missing values and duplicate records.
- Calculated average grades using G1, G2, and G3.
- Created project-defined performance categories.
- Compared weekly study-time categories with final grades.
- Calculated summary statistics using NumPy.

## Visualizations

1. Bar chart: Average grades across periods.
2. Scatter-style strip plot: Study-time category vs final grade.
3. Histogram: Distribution of final grades.
4. Pie chart: Student performance categories.

## Key Insights

The notebook calculates eight insights, including:

- Total number of students.
- Average, highest, and lowest final grades.
- Average grades across three periods.
- Study-time category with the highest average final grade.
- Counts of students in each performance category.

## Project Files

- `student-mat.csv`
- `Student_Performance_Analysis.ipynb`
- `insight_summary.txt`
- `README.md`
- `screenshots/`
- `project_demo.mp4` (if included)

## How to Run

1. Install Python.
2. Install the required libraries:

   `pip install pandas numpy matplotlib seaborn jupyter`

3. Open `Student_Performance_Analysis.ipynb` in VS Code.
4. Select a Python kernel.
5. Ensure `student-mat.csv` is in the same folder as the notebook.
6. Run all notebook cells in order.

## Learning Outcomes

Practiced working with a real dataset, data exploration, data cleaning,
Pandas operations, NumPy statistics, visualization, and insight generation.
