import speech_recognition as sr
import sounddevice as sd

import numpy as np


def record_audio(duration, fs=44100):

    r = sr.Recognizer()
    with sr.Microphone(sample_rate=fs) as source:
        print("Speak now...")
        audio_data = r.record(source, duration=duration)
        print("Recording finished.")
    return audio_data


r = sr.Recognizer()
def speech_recognition(audio_data, language="en-US"):
    global r
    try:
        text = r.recognize_google(audio_data, language=language)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        return 0


audio_data = record_audio(duration=1)

text=speech_recognition(audio_data, language="en-US")
print(text)