import pyttsx3
import speech_recognition as sr  # Import the speech_recognition module

engine = pyttsx3.init()
r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)  # Corrected variable name
            print("Please say something...")
            print("Listening...")
            audio = r.listen(source)
            print("Recognizing...")
            text = r.recognize_google(audio, language='en-US')
            text = text.lower()
            
        if "stop" in text:
            print("Stopping the program.")
            break
        else:
            # Print the recognized text
            print(f"You said: {text}")
            engine.say(text)  
            engine.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")