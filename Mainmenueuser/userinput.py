import tensorflow as tf
import os
# from tflite_runtime.interpreter import Interpreter
from MAIN_Proj import Slidingwind as S_w
from scipy.io import wavfile
import numpy as np

# import read_audio as ra
import sounddevice as sd
import time

i = 0
full = np.empty(0)

sp = os.path.dirname(os.path.abspath(__file__)) + "/"


# for i in range(5):
def answer(First_time=True):
    # Load the TFLite model
    global i
    global full
    interpreter = tf.lite.Interpreter(model_path=sp + "yesno.tflite")

    # Allocate memory for the model
    interpreter.allocate_tensors()

    # Get the input and output tensors
    input_index = interpreter.get_input_details()
    output_index = interpreter.get_output_details()
    #    print(input_index)
    #    print(output_index)
    # Read the audio data
    # for k in reversed(range(2)):

    audio_generator = S_w.read_audio_data(First_time)
    #  print(k)
    audio_data = next(audio_generator)

    # time.sleep(2)
    # Preprocess the audio data
    # audio_data = preprocess_audio_data(audio_data)

    # Get the shape of the audio data
    # shape = audio_data.shape
    # print("shape is", shape)
    # Create a new tensor with the desired shape
    # for i in range(10):
    input_tensor = np.array(audio_data, dtype=np.int32)
    # Reshape the input tensor to the required shape
    input_tensor = audio_data[:44032].reshape(1, 44032)
    # print("playing!")
    audio_data = audio_data[:44032]
    # sd.play(audio_data, 44100)
    # sd.wait()
    # Verify the shape of the input tensor
    #    print("Shape of input tensor:", input_tensor.shape)
    interpreter.set_tensor(0, input_tensor)
    # Run the model
    interpreter.invoke()
    output_details = interpreter.get_output_details()[0]
    prediction_tensor = interpreter.tensor(output_details['index'])
    predictions = prediction_tensor()
    #   print("Predictions:", predictions[0])
    array = [["Background_noise", 1], ["No", 1], ["Yes", 1]]
    max_val = predictions[0].argmax()
    #print(array[max_val][0], "with prediction", predictions[0][max_val])
    if predictions[0][max_val] < 0.5:
        max_val = 0


    print(array[max_val][0], "with prediction", predictions[0][max_val])
    res = array[max_val][0]
    wavfile.write(sp + f"Test_voice/Testaudio{res}.wav", 44032, audio_data)
    i += 1
    return array[max_val][0]

# def MA_AUDIOINPUT():

# S_w.audio_ini()
# while(1):
#     machine_learning_model()
# sd.play(full, 44100)
# sd.wait()
