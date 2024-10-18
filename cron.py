import time
import subprocess

while True:
    subprocess.run(["python", "your_script.py"])  # Replace 'your_script.py' with the name of your file
    time.sleep(60)  # Wait for 1 minute