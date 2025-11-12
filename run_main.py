import subprocess
import os

# --- Configuration ---
# The path to your SeiraTools project directory.
project_directory = "C:/Users/Owner/Downloads/SeiraTools"

# The path to the Python executable in your virtual environment.
python_executable = os.path.join(project_directory, ".venv", "Scripts", "python.exe")

# The path to the script you want to run.
script_to_run = os.path.join(project_directory, "src", "main.py")
# --- End of Configuration ---

# Ensure paths are in the correct format for the operating system
project_directory = os.path.normpath(project_directory)
python_executable = os.path.normpath(python_executable)
script_to_run = os.path.normpath(script_to_run)

# The command to be executed, broken into a list of arguments
command = [python_executable, script_to_run]

print(f"Attempting to run command: {' '.join(command)}")
print(f"Working directory: {project_directory}\n")

try:
    # Execute the command
    process = subprocess.run(
        command,
        cwd=project_directory, # Set the working directory
        check=True,          # Raise an exception if the command fails
        capture_output=True, # Capture the command's stdout and stderr
        text=True            # Decode stdout/stderr as text (UTF-8)
    )

    print("--- Script executed successfully ---")
    if process.stdout:
        print("\n--- Output (STDOUT) ---")
        print(process.stdout)
    if process.stderr:
        print("\n--- Errors (STDERR) ---")
        print(process.stderr)

except FileNotFoundError:
    print(f"Error: Could not find the file.")
    print(f"Please check if this path is correct: {python_executable}")
except subprocess.CalledProcessError as e:
    print(f"--- An error occurred while running the script (Exit Code: {e.returncode}) ---")
    if e.stdout:
        print("\n--- Output (STDOUT) ---")
        print(e.stdout)
    if e.stderr:
        print("\n--- Errors (STDERR) ---")
        print(e.stderr)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
