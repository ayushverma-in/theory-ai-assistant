import time
import os
import webbrowser
from datetime import datetime
import pyttsx3
import speech_recognition as sr
import pyautogui
from rapidfuzz import fuzz
import ctypes      
import feedparser    
from PIL import ImageGrab
import requests

# INITIALIZE 

engine = pyttsx3.init()
recognizer = sr.Recognizer()

# SPEAK 

def speak(text):
    print("Theory:", text)
    engine.say(text)
    engine.runAndWait()

# VOLUME CONTROL 

def set_volume(percent):
    devices = ctypes.windll.user32
    devices.waveOutSetVolume(0, int(percent * 65535 / 100) + (int(percent * 65535 / 100) << 16))

def mute_volume():
    ctypes.windll.user32.keybd_event(173, 0, 0, 0) 

def increase_volume():
    ctypes.windll.user32.keybd_event(175, 0, 0, 0) 

def decrease_volume():
    ctypes.windll.user32.keybd_event(174, 0, 0, 0) 

# NEWS HEADLINES

def get_news():
    url = "http://feeds.bbci.co.uk/news/rss.xml"  
    feed = feedparser.parse(url)
    
    if not feed.entries:
        return []
    
    headlines = [entry.title for entry in feed.entries[:5]] 
    return headlines

# LISTEN

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        speak("Say that again please")
        return ""
    
# MEMORY 

def save_memory(text):
    with open("memory.txt", "a") as file:
        file.write(text + "\n")

def read_memory():
    try:
        with open("memory.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

# UTILITY FUNCTIONS 

def is_match(command, keywords):
    for word in keywords:
        if word in command:
            return True
        if fuzz.partial_ratio(word, command) > 70:
            return True
    return False

def take_screenshot():
    try:
        screenshots_folder = os.path.expanduser(r"~/OneDrive/Pictures/Screenshots")
        
        if not os.path.exists(screenshots_folder):
            os.makedirs(screenshots_folder)
        
        timestamp = time.strftime("%Y-%m-%d %H%M%S")
        filename = f"Screenshot {timestamp}.png"
        save_path = os.path.join(screenshots_folder, filename)
        img = ImageGrab.grab()
        img.save(save_path)
        speak(f"Screenshot taken and saved at {save_path}")
        
    except Exception as e:
        speak(f"Failed to take screenshot: {e}")

# START 

speak("Hello, I am Theory. How can I help you?")

# MAIN LOOP 

while True:
    command = listen()
    if command == "":
        continue

    print("Command:", command)

    # Greetings
    if is_match(command, ["hello", "hi"]):
        speak("Welcome back sir. Theory is ready.")

    # Open websites / apps
    elif is_match(command, ["youtube", "yt"]):
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif is_match(command, ["chrome", "browser"]):
        os.system("start chrome")
        speak("Opening Chrome")

    elif is_match(command, ["notepad"]):
        os.system("notepad")
        speak("Opening Notepad")

    elif is_match(command, ["calculator", "calc", "calculate"]):
        os.system("calc")
        speak("Opening Calculator")

    # Time & Date
    elif is_match(command, ["time"]):
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif is_match(command, ["date"]):
        current_date = datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    # Google Search
    elif is_match(command, ["search", "google"]):
        speak("What should I search?")
        query = listen()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")

    # Screenshot
    elif is_match(command, ["screenshot", "screen"]):
        take_screenshot()

    # System Commands
    elif is_match(command, ["shutdown"]):
        speak("Shutting down the system")
        os.system("shutdown /s /t 5")

    elif is_match(command, ["restart"]):
        speak("Restarting the system")
        os.system("shutdown /r /t 5")

    elif is_match(command, ["exit", "stop", "close"]):
        speak("Shutting down. Goodbye boss")
        break

    # VOLUME CONTROL 
    elif is_match(command, ["mute volume", "mute sound"]):
        mute_volume()
        speak("Volume muted")

    elif is_match(command, ["volume up", "increase volume"]):
        increase_volume()
        speak("Volume increased")

    elif is_match(command, ["volume down", "decrease volume"]):
        decrease_volume()
        speak("Volume decreased")

# SYSTEM COMMANDS
    elif is_match(command, ["log off", "sign out"]):
        speak("Logging off")
        os.system("shutdown -l")

# NEWS HEADLINES 
    elif is_match(command, ["news", "headlines"]):
        speak("Fetching latest news headlines")
        try:
            news_list = get_news()
            if not news_list:
                speak("Sorry, I could not fetch any news.")
            else:
                for idx, headline in enumerate(news_list, 1):
                    speak(f"Headline {idx}: {headline}")
        except Exception as e:
            speak(f"Failed to fetch news: {e}")

    # Memory Commands
    elif "remember" in command:
        speak("What should I remember?")
        data = listen()
        save_memory(data)
        speak("Got it. I will remember that.")

    elif "what do you remember" in command or "show memory" in command:
        data = read_memory()
        if data:
            speak("Here is what I remember")
            print(data)
            speak(data)
        else:
            speak("I don't remember anything yet")

    else:
        speak("I cannot answer that right now.")