import os
import subprocess
from datetime import datetime

jmeter_executable = r"D:\apache-jmeter-5.5\apache-jmeter-5.5\bin\jmeter.bat" #Change it with you actual jmeter executable path

# Paths and configurations
jmx_files = [
    r"D:\WORK\Sample\Sample_file.jmx",
    r"D:\WORK\Sample\Sample_file2.jmx"
]
base_results_path = r"D:\WORK\Invision_BAP\VIPSAASQA_load_testing\Results"
configurations = ["10u60s", "50u60s", "100u60s", "200u120s", "500u180s"] # Your combination of Threads and Rampup period, 10u60s means 10 users and 60 seconds

# Create a parent directory for the current month
current_month = datetime.now().strftime("%B_%Y")
month_dir = os.path.join(base_results_path, current_month)
os.makedirs(month_dir, exist_ok=True)

# Iterate over JMX files and configurations
for jmx_file in jmx_files:
    jmx_name = os.path.splitext(os.path.basename(jmx_file))[0]
    jmx_dir = os.path.join(month_dir, jmx_name)
    os.makedirs(jmx_dir, exist_ok=True)

    for config in configurations:
        # Create subfolder for each configuration
        config_dir = os.path.join(jmx_dir, config)
        os.makedirs(config_dir, exist_ok=True)

        # Parse threads and ramp-up period from the configuration
        threads, ramp_up = config.split('u')
        ramp_up = ramp_up.rstrip('s')  # Remove 's' if present

        # Define result file paths
        result_csv = os.path.join(config_dir, "Results.csv")
        result_html = config_dir  # Output folder for HTML report

        # Construct the JMeter command
        command = [
            jmeter_executable,
            "-n", "-t", jmx_file,  # Non-GUI mode and JMX file
            "-l", result_csv,  # Save results to a CSV file
            "-e", "-o", result_html,  # Generate HTML report in the config directory
            "-Jthreads", threads,  # Pass thread count dynamically
            "-Jrampup", ramp_up  # Pass ramp-up time dynamically
        ]

        # Execute the JMeter command
        try:
            print(f"Running JMeter for {jmx_name} with configuration {config}...")
            subprocess.run(command, check=True)
            print(f"Results saved in {config_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error running JMeter for {jmx_name} with {config}: {e}")
