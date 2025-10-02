import speech_recognition as sr 

key = "locked"
password = "2020"
audio = None
while audio not in ["2020","two zero two zero"]:
    rec = sr.Recognizer()
    with sr.Microphone() as src:
        print("say password ...")
        audiodata = rec.recognize_google_cloud(src)
        print(key)
        print(audiodata)
else:
    key = "unlocked"
    print(f"you have said the correct password")
    print(audiodata)