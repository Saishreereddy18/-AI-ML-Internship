# Day 20 – Tool Selection Matrix

## 1. Objective

The purpose of this matrix is to identify the correct tool or function for a user request. Selecting the right tool improves accuracy, efficiency, and reliability.

## 2. Tool Selection Decision Table

| S.No. | User Request                                         | Tool / Function               | Reason                                                        |
| ----- | ---------------------------------------------------- | ----------------------------- | ------------------------------------------------------------- |
| 1     | What is 25 multiplied by 4?                          | Calculator                    | Performs mathematical calculations accurately.                |
| 2     | Find the latest AI news.                             | Web Search                    | Retrieves current information from online sources.            |
| 3     | Find employee details by name.                       | Database Tool                 | Searches structured employee records.                         |
| 4     | Read the contents of a PDF file.                     | File Reader                   | Extracts text from a supported document.                      |
| 5     | What is the current weather in Hyderabad?            | Weather Tool                  | Retrieves current weather information from a weather service. |
| 6     | Send a meeting reminder email.                       | Email Tool                    | Creates or sends an email with appropriate authorization.     |
| 7     | What is today's date?                                | Date Tool                     | Returns the current system date.                              |
| 8     | Calculate the average salary in a CSV file.          | Data Analyzer                 | Processes numerical data and calculates statistics.           |
| 9     | Find employees in the AI department.                 | Company Data Query Tool       | Filters employee records by department.                       |
| 10    | Search for an employee and analyze their department. | Search + Data Analyzer        | Chains tools to retrieve records and analyze the results.     |
| 11    | Find the total number of employees.                  | Database Tool / Data Analyzer | Counts employee records from the available dataset.           |
| 12    | The requested CSV file is missing.                   | Error Handler                 | Detects the missing file and returns a helpful error message. |

## 3. Decision-Making Rules

1. Identify the user's intent.
2. Select the tool that best matches the request.
3. Check whether the required input is available.
4. Execute the tool or function.
5. Validate the result.
6. Handle errors safely.
7. Return a clear response to the user.

## 4. Conclusion

The Tool Selection Matrix helps an AI system select the correct function for different requests. It supports accurate tool selection, function calling, tool chaining, and error handling.
