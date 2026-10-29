
import pandas as pd
from pathlib import Path
from datetime import datetime

# Dataset path
DATA_FILE = Path(__file__).parent / "data" / "company_data.csv"


# 1. Load and validate company data
def load_company_data():
    """Load company data and validate required columns."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)

    required_columns = {
        "Employee_ID",
        "Name",
        "Department",
        "Role",
        "Salary",
        "Experience"
    }

    missing = required_columns - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns: {sorted(missing)}"
        )

    if df.empty:
        raise ValueError("The company dataset is empty.")

    return df


# 2. Search employees by name
def search_employee(name):
    """Search employee records using a name."""
    if not name or not name.strip():
        raise ValueError("Employee name cannot be empty.")

    df = load_company_data()

    return df[
        df["Name"].astype(str).str.contains(
            name.strip(), case=False, na=False, regex=False
        )
    ]


# 3. Filter employees by department
def filter_department(department):
    """Return employees belonging to a department."""
    if not department or not department.strip():
        raise ValueError("Department cannot be empty.")

    df = load_company_data()

    return df[
        df["Department"].astype(str).str.strip().str.lower()
        == department.strip().lower()
    ]


# 4. Analyze company data
def analyze_company_data():
    """Calculate statistics for the company dataset."""
    df = load_company_data()

    return {
        "total_employees": len(df),
        "departments": df["Department"].nunique(),
        "average_salary": round(df["Salary"].mean(), 2),
        "average_experience": round(df["Experience"].mean(), 2),
        "missing_values": int(df.isnull().sum().sum())
    }


# 5. Get the current date
def get_date():
    """Return the current system date."""
    return datetime.now().strftime("%Y-%m-%d")


# 6. Tool chaining: filter employees and analyze salaries
def chain_department_analysis(department):
    """Filter employees, then calculate their average salary."""
    employees = filter_department(department)

    if employees.empty:
        return "No employees found in that department."

    average_salary = round(employees["Salary"].mean(), 2)

    return {
        "department": department.strip(),
        "employee_count": len(employees),
        "average_salary": average_salary,
        "employees": employees["Name"].tolist()
    }


# 7. Registered tool functions
def call_tool(tool_name, argument=""):
    """Select and execute an approved tool."""
    tools = {
        "search_employee": lambda: search_employee(argument),
        "filter_department": lambda: filter_department(argument),
        "analyze_data": analyze_company_data,
        "get_date": get_date,
        "chain_analysis": lambda: chain_department_analysis(argument)
    }

    if tool_name not in tools:
        return f"Error: Unknown tool '{tool_name}'."

    try:
        result = tools[tool_name]()

        if isinstance(result, pd.DataFrame):
            if result.empty:
                return "No matching records found."

            return result.to_string(index=False)

        return result

    except FileNotFoundError as error:
        return f"File error: {error}"

    except (ValueError, pd.errors.ParserError) as error:
        return f"Data error: {error}"

    except Exception as error:
        return f"Unexpected error: {error}"


# 8. Main application menu
def main():
    print("\n===== COMPANY DATA QUERY TOOL =====")
    print("1. Search employee")
    print("2. Filter department")
    print("3. Analyze company data")
    print("4. Get current date")
    print("5. Filter department and analyze salary")
    print("0. Exit")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        name = input("Enter employee name: ").strip()
        print(call_tool("search_employee", name))

    elif choice == "2":
        department = input("Enter department: ").strip()
        print(call_tool("filter_department", department))

    elif choice == "3":
        print(call_tool("analyze_data"))

    elif choice == "4":
        print("Current date:", call_tool("get_date"))

    elif choice == "5":
        department = input("Enter department: ").strip()
        print(call_tool("chain_analysis", department))

    elif choice == "0":
        print("Thank you for using the Company Data Query Tool!")

    else:
        print("Invalid choice. Please select 0, 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
