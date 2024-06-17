import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id) to see voice options
engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
    speak("good morning bhargav sir your buddy jarvis this side  tell me how  may i help you")

    elif hour>=12 and hour<18:
        speak("good afternoon bhargav sir your buddy jarvis this side tell me how  may i help you")
    else:
           speak("good evening bhargav sir your buddy jarvis this side tell me how  may i help you") 

if __name__ == "__main__":
    speak("bhargav is a good boy")
