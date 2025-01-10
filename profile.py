from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to the Chrome profile
chrome_profile_path = "C:\\Users\\<YourUsername>\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"

# Set up Chrome options
options = Options()
options.add_argument(f"user-data-dir={chrome_profile_path}")

# Initialize the WebDriver
service = Service("path/to/chromedriver")  # Replace with the path to your ChromeDriver
driver = webdriver.Chrome(service=service, options=options)

# Open a website
driver.get("https://www.google.com")

# Perform your actions
print("Current URL:", driver.current_url)

# Close the browser
driver.quit()