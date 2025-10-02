import speech_recognition as sr 

rec = sr.Recognizer()
with sr.Microphone() as src:
    print("say something ...")
    audio = rec.recognize_google(src)
print(audio)