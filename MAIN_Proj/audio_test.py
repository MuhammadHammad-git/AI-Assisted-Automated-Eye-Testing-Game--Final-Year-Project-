from MAIN_Proj import Slidingwind as sw
import numpy as np
import sounddevice as sd
from scipy.io import wavfile
MA_audio_len = 44032
i = 0
dual = np.empty(0)
full = np.empty(0)
sw.audio_ini()
while i < 3:
    file = f"Test_voice/audio{i}.wav"
    
    # record audio data
    audio = sw.read_audio_data(True)
    dual = next(audio)
    print(len(dual))
    dual = dual[:MA_audio_len]
    # check if the recording has a sufficient length and sample rate
    
    if len(dual) < MA_audio_len:
        print(f"Recording {i} is too short!")
    if len(dual) > MA_audio_len:
        print(f"Recording {i} is Resizable!")
    
    # write the recording to a wave file
    wavfile.write(file, MA_audio_len, dual)
    
    if i == 0:
        full = dual
    else:
        full = np.vstack((full, dual))
    i += 1

# play the full recording
sd.play(full, MA_audio_len)
sd.wait()
print("Done")