# Day 20 – Workflow Notes

## 1. Project Overview

The Company Data Query Tool is a Python-based application that searches employee records, filters departments, analyzes company data, and retrieves the current date.

It demonstrates tool creation, function calling, tool chaining concepts, and error handling.

## 2. Workflow Architecture

User Request
|
v
Input Validation
|
v
Function Selection
|
v
Tool Execution
|
v
Result Validation
|
v
Output or Error Message

## 3. Workflow Steps

### Step 1: Receive Input

The application displays a menu and accepts the user's choice.

### Step 2: Validate Input

The application checks whether the selected option and required input are valid.

### Step 3: Select a Function

The call_tool() function identifies the requested function using the registered tool dictionary.

### Step 4: Execute the Tool

The selected function performs the requested operation:

- search_employee() searches employee names.
- filter_department() filters employee records.
- analyze_company_data() calculates dataset statistics.
- get_date() returns the current date.

### Step 5: Process Results

The application formats matching records or returns the calculated summary.

### Step 6: Handle Errors

The application handles missing files, missing columns, invalid tool names, and common data-reading errors.

### Step 7: Display Output

The final result or a helpful error message is displayed in the terminal.

## 4. Tool Chaining Example

Request:
"Find employees in the AI department and calculate their average salary."

Workflow:

1. Load the company CSV file.
2. Filter employees in the AI department.
3. Calculate the average salary of the filtered records.
4. Display the employees and their average salary.

This demonstrates how multiple functions can work together to solve a single request.

Note: This chained workflow is a design example. The current implementation does not yet automatically calculate the average salary of filtered results.

## 5. Error Handling Strategy

| Error                   | Expected Handling                     |
| ----------------------- | ------------------------------------- |
| Missing dataset         | Display a file error                  |
| Missing required column | Display a data validation error       |
| Invalid menu choice     | Ask the user to choose a valid option |
| Empty search input      | Display an input validation message   |
| No matching employee    | Display a no-records message          |
| Invalid tool name       | Return an unknown-tool error          |

## 6. Testing Plan

1. Search for an existing employee.
2. Search for a name that does not exist.
3. Filter employees by the AI department.
4. Analyze the company dataset.
5. Retrieve the current date.
6. Enter an invalid menu option.
7. Test the error handling for a missing or invalid dataset.

## 7. Expected Outcome

The application should select the appropriate function, process company records, return accurate results, and report common errors clearly.

## 8. Conclusion

The workflow demonstrates how small Python functions can be organized into a reusable tool system. The design can later be extended with database queries, web search, weather APIs, email integration, and AI-based tool selection.
