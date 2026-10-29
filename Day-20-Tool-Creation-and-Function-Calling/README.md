# Day 20 – Tool Creation and Function Calling

## Project: Company Data Query Tool

### 1. Project Overview

The Company Data Query Tool is a Python-based application designed to demonstrate tool creation, function calling, tool chaining, and error handling.

The application works with a sample company employee dataset to search employee records, filter employees by department, analyze company data, and retrieve the current date.

This project demonstrates how individual Python functions can be organized into a reusable tool system that processes user requests and returns meaningful results.

### 2. Learning Objectives

- Understand tool creation and function calling.
- Select the appropriate function based on a user request.
- Implement tool chaining for multi-step operations.
- Validate user inputs and handle errors.
- Analyze structured company data using Python.
- Document tool selection decisions and workflow design.

### 3. Technologies Used

- **Programming Language:** Python
- **Library:** Pandas
- **Data Format:** CSV
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

### 4. Project Structure

```text
Day-20-Tool-Creation-and-Function-Calling/
│
├── data/
│   └── company_data.csv
│
├── company_tool.py
├── Tool_Selection_Matrix.md
├── Function_Calling_Documentation.md
├── Workflow_Notes.md
├── requirements.txt
└── README.md
```

### 5. Implemented Features

1. **Employee Search:** Searches employee records by name.
2. **Department Filtering:** Retrieves employees belonging to a specified department.
3. **Company Data Analysis:** Calculates employee count, number of departments, average salary, average experience, and missing-value count.
4. **Date Tool:** Retrieves the current system date.
5. **Tool Selection:** Uses a registered function dictionary to select the requested function.
6. **Tool Chaining:** Filters employees by department and calculates their average salary.
7. **Error Handling:** Handles missing files, missing required columns, invalid tool names, invalid data, and empty search results.
8. **Input Validation:** Checks required employee names and department names.

### 6. Installation

Make sure Python is installed and open the project folder in VS Code.

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
pandas
```

### 7. How to Run

Run the following command in the VS Code terminal:

```bash
python company_tool.py
```

The application displays a menu with the following options:

| Option | Function                             |
| ------ | ------------------------------------ |
| 1      | Search employee                      |
| 2      | Filter department                    |
| 3      | Analyze company data                 |
| 4      | Get current date                     |
| 5      | Filter department and analyze salary |
| 0      | Exit                                 |

Select an option and enter the requested information.

### 8. Sample Dataset

The sample dataset contains 10 fictional employee records with these columns:

- Employee_ID
- Name
- Department
- Role
- Salary
- Experience

The records cover AI, Data, IT, and HR departments.

### 9. Expected Results

For the supplied sample dataset, the company analysis should report:

| Metric             | Expected result |
| ------------------ | --------------: |
| Total employees    |              10 |
| Departments        |               4 |
| Average salary     |          50,800 |
| Average experience |       2.2 years |
| Missing values     |               0 |

**Tool-chaining example:**

Input department: `AI`

Expected output:

- Employee count: 3
- Employees: Aarav, Meera, Vikram
- Average salary: 48,333.33

These results assume the original sample CSV has not been modified.

### 10. Tool Selection Matrix

The `Tool_Selection_Matrix.md` document contains 12 user requests, their corresponding tools or functions, and the reasons for selecting each tool.

The matrix covers calculator, web search, database, file reader, weather, email, date, data analysis, company employee search, tool chaining, and error handling.

### 11. Function Calling

The `call_tool()` function uses a dictionary of registered functions to select and execute the requested operation.

The current implementation supports employee search, department filtering, company data analysis, date retrieval, and chained department analysis.

### 12. Tool Chaining Workflow

The `chain_department_analysis()` function demonstrates a multi-step workflow:

1. Receive the department name.
2. Retrieve matching employee records.
3. Calculate the average salary of the matching employees.
4. Return the department, employee count, salary average, and employee names.

This approach demonstrates how multiple operations can be combined to fulfil a single request.

### 13. Error Handling

The application handles common problems, including:

- Missing CSV files.
- Missing required columns.
- Invalid or unreadable CSV data.
- Empty employee or department inputs.
- Unknown tool names.
- Departments with no matching employees.
- Invalid menu selections.
- Unexpected application interruptions.

Errors are reported through readable messages whenever possible.

### 14. Testing Plan

The following test cases can be used to verify the application:

| Test case                      | Expected result                            |
| ------------------------------ | ------------------------------------------ |
| Search for Meera               | Displays Meera's employee record           |
| Filter the AI department       | Displays three employees                   |
| Analyze company data           | Displays the expected statistics           |
| Retrieve the date              | Displays the current system date           |
| Run chained analysis for AI    | Displays employee names and average salary |
| Search for an unknown employee | Displays no matching records               |
| Enter an invalid menu option   | Displays an invalid-choice message         |
| Enter an unknown tool name     | Returns an unknown-tool error              |

### 15. Functionality Not Yet Integrated

The following tools are included in the documentation and selection matrix but are not connected to live services in this version:

- Calculator service
- Web Search
- External Database
- PDF/File Reader
- Weather API
- Email service

These can be implemented as future extensions using suitable APIs, libraries, and authorization.

The current application uses Python function selection; it does not yet use an LLM to autonomously choose tools.

### 16. Deliverables

- `Tool_Selection_Matrix.md` – Tool selection decision table.
- `Function_Calling_Documentation.md` – Function calling concepts, tool descriptions, chaining, and error handling.
- `Workflow_Notes.md` – Project architecture, workflow, and testing strategy.
- `company_tool.py` – Practical Python implementation.
- `data/company_data.csv` – Sample company dataset.
- `requirements.txt` – Required Python dependency.

### 17. Conclusion

The Day 20 project demonstrates the fundamentals of tool creation, function calling, tool chaining, and error handling through a practical Python application.

It provides a foundation for building more advanced AI agents that select and combine tools to perform multi-step tasks. Future improvements may include live APIs, database integration, document reading, and LLM-based tool selection.
