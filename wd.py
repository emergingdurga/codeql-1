from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
options = Options()
options.add_argument("user-data-dir=/Users/your_username/Library/Application Support/Google/Chrome/Profile 1")

# Automatically manage ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open a website
driver.get("https://www.google.com")

print("Page Title:", driver.title)

driver.quit()