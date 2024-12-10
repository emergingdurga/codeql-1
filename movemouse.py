import pyautogui
import time

# Total duration in seconds (5 hours)
duration = 5 * 60 * 60  
# Interval in seconds (20 seconds)
interval = 20  
start_time = time.time()

print("Mouse movement started. Press Ctrl+C to stop.")
try:
    while time.time() - start_time < duration:
        # Get current mouse position
        x, y = pyautogui.position()
        # Move the mouse slightly (1 pixel to the right)
        pyautogui.moveTo(x + 1, y)
        # Move it back to the original position
        pyautogui.moveTo(x, y)
        # Wait for the next interval
        time.sleep(interval)
except KeyboardInterrupt:
    print("\nMouse movement stopped.")