import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("Hey, I am Ziva. Please tell me how may I help you")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        print("Sorry, say it again...")
        return "None"
    return query.lower()


if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()
        if "wikipedia" in query:
            speak("Wikipedia searching...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            print(results)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")

        elif 'open hackerrank' in query:
            webbrowser.open("https://www.hackerrank.com")

        elif 'open whatsapp web' in query:
            webbrowser.open("https://web.whatsapp.com")

        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif "open code" in query:
            code_path = r"E:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code_path)

        elif "open chrome" in query:
            chrome_path = r"E:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome_path)

        elif 'send mail' in query:
            pass

        elif "goodbye" in query:
            speak("I think I was useful for you. Bye, have a nice day Har Har MAHADEV")
            exit()

