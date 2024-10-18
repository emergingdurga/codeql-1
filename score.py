import requests
from bs4 import BeautifulSoup
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_page_title(url):
    # Send a GET request to fetch the page content
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the page title
        title = soup.title.get_text(strip=True)
        print("Page Title:", title)
        speak(f"The page title is {title}")
    else:
        print("Failed to retrieve the page.")
        speak("Failed to retrieve the page.")

# URL of the live score page
url = "https://m.cricbuzz.com/live-cricket-scores/100265/ind-vs-nz-1st-test-new-zealand-tour-of-india-2024"
get_page_title(url)