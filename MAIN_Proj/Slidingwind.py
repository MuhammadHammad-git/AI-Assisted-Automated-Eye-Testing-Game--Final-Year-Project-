import numpy as np
import math as m
import sounddevice as sd

Second_Half = np.empty(0)
prev_Half = np.empty(0)
First_Half = np.empty(0)
recording2 = np.empty(0)
#First_Time = True
send_prev = False
record = True


def read_audio_data(First_Time = True, duration=1, fs=44100):
    global prev_Half, First_Half, Second_Half, send_prev, recording2, record
    audio_size = duration * fs
    if First_Time:
        print("Speak!")        
        recording = sd.rec(int(audio_size), samplerate=fs, channels=1, blocking=False)
        sd.wait()
        print("Done")
        audio_Hsize= (m.ceil(audio_size/2))
        Second_Half = recording[audio_Hsize::]
    else:
        if not send_prev:
            
            print("Speak!")
            recording = sd.rec(int(audio_size), samplerate=fs, channels=1, blocking=False)
            sd.wait()
            print("Done")
            #print(Second_Half)
            audio_Hsize= (m.ceil(audio_size/2))
            prev_Half = Second_Half
            Second_Half = recording[audio_Hsize::]
            First_Half = recording[:audio_Hsize:]

            recording2 = recording

            recording = np.vstack((prev_Half, First_Half))

            send_prev = True
        else:
            print("Previous value")
            recording = recording2
            send_prev = False
    yield recording
def audio_ini(duration=3, fs=44100):
    print("Initializing audio!")
    sd.rec(int(duration * fs), samplerate=fs, channels=1, blocking=False)
    sd.wait()
    print("Initialized")
    