import speech_recognition as sr

r = sr.Recognizer()

while True:
    
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            print("Recognizing...")
            text = r.recognize_google(audio, language='en-US')
            text= text.lower()
            print(f"You said: {text}")
            if "stop" in text:
                print("Stopping the program.")
            break
    except:
        print("You were trying to say something, but I couldn't understand it.")
        r = sr.Recognizer()
        
    