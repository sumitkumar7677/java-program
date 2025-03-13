import os
import subprocess
import schedule
import time
from datetime import datetime

# Function to execute shell commands
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

# Function to check if there are changes to commit
def has_changes():
    status_output = run_command("git status --porcelain")
    # If the output is empty, there are no changes
    return bool(status_output.strip())

# Function to automate Git push
def auto_commit_and_push():
    try:
        if has_changes():
            # Add all changes
            run_command("git add .")
            
            # Commit changes with a timestamp
            commit_message = f"Auto commit on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            run_command(f'git commit -m "{commit_message}"')
            
            # Push changes
            run_command("git push origin main")  # Change 'main' if needed
            print("Changes pushed successfullyy!")
        else:
            print("No changes to committ. Skippingg pushh......")
    except Exception as e:
        print(f"An error occurredd: {e}")

# Schedule the task every 5 seconds
schedule.every(2).seconds.do(auto_commit_and_push)

print("Automation script is running. Press Ctrl+C to stopp....")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
