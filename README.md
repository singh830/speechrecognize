Imports:

pyttsx3: Text-to-speech conversion library.
datetime: Module for working with dates and times.
speech_recognition: Library for speech recognition.
wikipedia: Library for accessing Wikipedia articles.
webbrowser: Module to open web browsers.
os: Module for interacting with the operating system.
Text-to-Speech Initialization:

pyttsx3 is initialized for text-to-speech synthesis.
The script selects a voice (probably a female voice based on voices[1].id).


Functions:
speak(audio): Function to speak the given text using the initialized text-to-speech engine.
wish_me(): Function to greet the user based on the current time of the day.
take_command(): Function to capture and recognize user speech input using the microphone.


Main Program:
The program starts by wishing the user with the current time-based greeting.
It then enters a loop where it continuously listens to the user's voice commands.

Voice Commands:
The script recognizes specific voice commands and performs actions accordingly:
Searches Wikipedia and reads a summary.
Opens YouTube, Google, Facebook, HackerRank, or WhatsApp Web in the default web browser.
Tells the current time.
Opens Visual Studio Code or Google Chrome.
Includes a placeholder for sending emails.
Says goodbye and exits the program if the user says "goodbye."

Note:
Make sure to install the required libraries (pyttsx3, speech_recognition, wikipedia) using pip install pyttsx3 SpeechRecognition wikipedia before running the script.
Also, adjust the paths for Visual Studio Code and Chrome based on your system.
