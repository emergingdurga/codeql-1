import requests
from bs4 import BeautifulSoup
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_live_score(url):
    # Send a GET request to fetch the page content
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the section containing the score. This may vary depending on page structure.
        # Assuming score is under a div with a specific class related to score
        score_tag = soup.find('div', class_='cb-ltst-wgt-hdr')
        
        if score_tag:
            score = score_tag.get_text(strip=True)
            print("Current score:", score)
            speak(f"The current score is {score}")
        else:
            print("Could not find the score.")
            speak("Could not find the score.")
    else:
        print("Failed to retrieve the page.")
        speak("Failed to retrieve the page.")

# URL of the live score page
url = "https://m.cricbuzz.com/live-cricket-scores/100265/ind-vs-nz-1st-test-new-zealand-tour-of-india-2024"
get_live_score(url)