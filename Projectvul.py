import os
import subprocess

# Path where all projects are stored
projects_directory = ''
# Output file for storing the vulnerabilities report
output_file = 'vulnerabilities_report.txt'

def scan_project(project_path):
    """Run the vulnerability scan for a single project."""
    try:
        # Run the Bandit tool to scan the project for vulnerabilities
        # Replace 'bandit' with the appropriate tool for your project type
        result = subprocess.run(['bandit', '-r', project_path], capture_output=True, text=True)
        
        # Capture and return the output from the scan
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return f"Failed to scan project {project_path}: {str(e)}"

def scan_all_projects(projects_directory, output_file):
    """Scan all projects in the directory and write the results to an output file."""
    with open(output_file, 'w') as report:
        # Iterate through each project in the directory
        for project_name in os.listdir(projects_directory):
            project_path = os.path.join(projects_directory, project_name)

            if os.path.isdir(project_path):
                report.write(f"Scanning project: {project_name}\n")
                report.write(f"{'-'*50}\n")

                # Scan the project for vulnerabilities
                vulnerabilities = scan_project(project_path)
                
                # Write the vulnerabilities to the report
                report.write(vulnerabilities)
                report.write(f"{'='*50}\n\n")
                print(f"Finished scanning {project_name}")

        print(f"Vulnerability report generated at: {output_file}")

if __name__ == "__main__":
    # Run the vulnerability scanning process
    scan_all_projects(projects_directory, output_file)
