from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import pyttsx3
import webbrowser
import datetime
import pyjokes
import os
import speech_recognition as sr
import schedule
import time
from threading import Thread

app = Flask(__name__)
CORS(app)

def speechtx(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 130)
    engine.say(text)
    engine.runAndWait()

def open_application(application):
    application = application.lower()
    if application == "ms excel":
        os.system("start excel")
        speechtx("Opening Microsoft Excel.")
    elif application == "music player":
        os.system("start spotify")
        speechtx("Opening the music player.")
    elif application == "notepad":
        os.system("start notepad")
        speechtx("Opening Notepad.")
    elif application == "web browser":
        webbrowser.open("https://www.google.com")
        speechtx("Opening the web browser.")
    elif application == "whatsapp":
        webbrowser.open("https://web.whatsapp.com/")
        speechtx("Opening WhatsApp.")
    elif application == "calculator":
        os.system("start calc")
        speechtx("Opening the calculator.")
    elif application == "ms word":
        os.system("start winword")
        speechtx("Opening Microsoft Word.")
    elif application == "ms powerpoint":
        os.system("start powerpnt")
        speechtx("Opening Microsoft PowerPoint.")
    elif application == "cmd":
        os.system("start cmd")
        speechtx("Opening Command Prompt.")
    elif application == "task manager":
        os.system("start taskmgr")
        speechtx("Opening Task Manager.")
    elif application == "file explorer":
        os.system("explorer")
        speechtx("Opening File Explorer.")
    elif application == "vlc player":
        os.system("start vlc")
        speechtx("Opening VLC Player.")
    elif application == "chrome":
        os.system("start chrome")
        speechtx("Opening Google Chrome.")
    elif application == "edge":
        os.system("start msedge")
        speechtx("Opening Microsoft Edge.")
    elif application == "shutdown":
        os.system("shutdown /s /t 1")
        speechtx("Shutting down the system.")
    elif application == "restart":
        os.system("shutdown /r /t 1")
        speechtx("Restarting the system.")
    elif application == "log off":
        os.system("shutdown /l")
        speechtx("Logging off the system.")
    else:
        speechtx("Sorry, I don't know how to open that application.")

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open_new_tab(url)  # Open search in a new tab
    speechtx(f"Searching for {query} on Google.")

def process_command(command):
    command = command.lower()
    if "your name" in command:
        speechtx("My name is Peter.")
    elif "old are you" in command:
        speechtx("I am two years old.")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speechtx(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speechtx(f"Today's date is {current_date}.")
    elif "joke" in command:
        joke = pyjokes.get_joke()
        speechtx(joke)
    elif "open" in command:
        application = command.replace("open ", "").strip()
        open_application(application)
    elif "search" in command:
        query = command.replace("search ", "").strip()
        search_google(query)
    elif "shutdown" in command:
        speechtx("Shutting down the assistant. Goodbye!")
        exit()
    else:
        search_google(command)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    command = data.get('command')
    if command:
        process_command(command)
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': 'No command received'}), 400

if __name__ == "__main__":
    app.run(debug=True)
