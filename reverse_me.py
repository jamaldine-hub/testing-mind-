import pyttsx3
import speech_recognition as sr
# second update reverse me function
def reverse_me():
    engine = pyttsx3.init()
    rec = sr.Recognizer()
    with sr.Microphone() as src:
        print("Say something ...")
        audio = rec.recognize_google(src)
        print(f"you said {audio}")
    audio = audio[::-1]
    print(f"your reverse {audio}")
    engine.say(audio)
    engine.runAndWait()
reverse_me()