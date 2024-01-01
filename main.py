import numpy as np
import tensorflow as tf
from tensorflow.keras import models

from recording_helper import record_audio, terminate
from tf_helper import preprocess_audiobuffer

# !! Modify this in the correct order
#commands = ['left', 'down', 'stop', 'up', 'right', 'no', 'go', 'yes']
commands = ['down', 'go', 'left', 'no', 'right', 'stop', 'up', 'yes']

loaded_model = models.load_model("saved_model")

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    print("prediction")
    print(prediction)
    print("Prediction[0]:")
    print(prediction[0])
    print("Value in prediction on position 1 prediction[0][0]")
    print(prediction[0][0])
    # maxValue = tf.maximum(prediction, 0)
    # print("Max value"+maxValue)
    maxValueInPrediction = tf.reduce_max(np.array(prediction))
    print("max value")
    print(maxValueInPrediction)
    if maxValueInPrediction > 0.9:
        label_pred = np.argmax(prediction, axis=1)
        print("Label_pred")
        print(label_pred)
        print("label_pred[0]")
        print(label_pred[0])
        # command = commands[label_pred[0]]
        command = commands[label_pred[0]]
        print("Predicted label label_pred[0]:", label_pred[0])
        print("Predicted label:", command)
        return command
    else:
        print("Not recognize the command")


if __name__ == "__main__":
    from turtle_helper import move_turtle
    while True:
        command = predict_mic()
        move_turtle(command)
        if command == "stop":
            terminate()
            break
        elif command == "up":
            terminate()