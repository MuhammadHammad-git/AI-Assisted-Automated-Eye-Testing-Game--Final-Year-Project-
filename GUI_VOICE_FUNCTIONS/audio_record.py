import sounddevice as sd

def read_audio_data(duration=1, fs=44100):
    audio_size = duration * fs

    print("Speak!")

    recording = sd.rec(int(audio_size), samplerate=fs, channels=1, blocking=False)
    sd.wait()

    print("Done--Recorded!")

    return recording

def play_audio_data(audio, fs=44100):

    print("Play!")
    sd.play(data=audio, samplerate=fs, blocking=False)
    sd.wait()
    print("Done--Playing!")

recorded_audio = read_audio_data()
play_audio_data(recorded_audio)