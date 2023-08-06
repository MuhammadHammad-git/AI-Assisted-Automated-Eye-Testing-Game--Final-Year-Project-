
def speech_recognition(audio_data, language="en-US"):

    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio_data, language=language)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        return 0