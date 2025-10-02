import pyttsx3
import speech_recognition as sr
# repeat me function
def repeat_me():
    engine = pyttsx3.init()
    rec = sr.Recognizer()
    with sr.Microphone() as src:
        print("Say something ...")
        audio = rec.recognize_google(src)
        print(f"you said {audio}")
    engine.say(audio)
    engine.runAndWait()
repeat_me()