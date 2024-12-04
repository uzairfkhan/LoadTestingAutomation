# Dynamic JMeter Test Runner

A Python script to automate the execution of JMeter `.jmx` test plans with dynamic thread and ramp-up configurations. This tool simplifies load testing workflows by organizing results and generating reports for each configuration.

## Features
- Batch execution of multiple `.jmx` test plans.
- Dynamically sets thread count and ramp-up period for each test run.
- Saves results in a structured directory hierarchy:
  - Organized by current month.
  - Subfolders for each `.jmx` file and its respective configurations.
- Outputs CSV results and HTML reports for detailed analysis.

## Requirements
- Python 3.7 or higher.
- Apache JMeter installed and added to your system's PATH or provide its executable path.

## Setup
1. Clone the repository:
   
   git clone https://github.com/uzairfkhan/LoadTestingAutomation


2. Install dependencies (if any are added later):

   pip install -r requirements.txt

3. Verify that Apache JMeter is installed:
   jmeter -v
   Alternatively, specify the full path to `jmeter.bat` in the script.

## Usage
1. **Update `.jmx` Files**:  
   Edit the `.jmx` files to include placeholders for dynamic configurations:
   - **Number of Threads (users)**: `${__P(threads,10)}`
   - **Ramp-Up Period (seconds)**: `${__P(rampup,60)}`

2. **Configure the Script**:  
   Update the script with:
   - Paths to your `.jmx` files.
   - Base results directory.
   - Desired thread and ramp-up configurations.

3. **Run the Script**:
   Execute the script using Python:
   python jmeter_runner.py

4. **View Results**:
   Results are saved in the specified base directory, organized by:
   <base_directory>/<current_month>/<jmx_file_name>/<configuration>/Results.csv

## Example Directory Structure
```
D:/WORK/Sample/
│
├── November_2024/
│   ├── Sample_File/
│   │   ├── 10u60s/
│   │   │   ├── Results.csv
│   │   │   ├── index.html
│   │   │   ├── ...
│   │   ├── 50u60s/
│   │   │   ├── Results.csv
│   │   │   ├── index.html
│   │   │   ├── ...
│   ├── Sample_file2/
│   │   ├── 10u60s/
│   │   ├── 50u60s/
│   │   ├── ...
```

## Configuration Details
- **Threads and Ramp-Up Periods**: Defined in the `configurations` list as `threads`u`rampup`s. For example:
  configurations = ["10u60s", "50u60s", "100u60s", "200u120s", "500u180s"]

- **JMeter Executable Path**:  
   Update the `jmeter_executable` variable in the script with the path to your JMeter binary (if not in PATH):
   jmeter_executable = r"D:\path\to\apache-jmeter\bin\jmeter.bat"

## Troubleshooting
- Ensure `.jmx` files use property placeholders for `threads` and `rampup`.
- Verify that JMeter is correctly installed and accessible from the command line.
- Check for permission issues in the results directory.
