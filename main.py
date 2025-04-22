import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()

while True:
    
    try:
        with sr.Microphone() as source:
            rs.adjust_for_ambient_noise(source, duration=0.2)
            print("Please say something...")
            print("Listening...")
            audio = r.listen(source)
            print("Recognizing...")
            text = r.recognize_google(audio, language='en-US')
            text= text.lower()
            
        if "stop" in text:
            print("Stopping the program.")
            break
        else:
            # Print the recognized text
            print(f"You said: {text}")
            engine.say(text)  
            engine.runAndWait()
            

        
    except sr.UnknownValueError:
        print("You were trying to say something, but I couldn't understand it.")
        r = sr.Recognizer()
        continue
    