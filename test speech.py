import speech_recognition as sr


def herken_stem() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Listening...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said:", text)
                return text.lower()
            except:
                print("Couldn't hear you, please try again.")


herken_stem()
