import pyttsx3 

user_input = input("Say something ... : ")
engine = pyttsx3.init()
engine.say(user_input)
engine.runAndWait()