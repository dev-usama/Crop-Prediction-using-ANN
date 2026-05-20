# Importing Libraries
from flask import Flask, request
import tensorflow as tf
import joblib
import numpy as np
from pathlib import Path

dir = Path(__file__).parent

scaler = joblib.load(dir / 'scalers/crp_scaler_ann.pkl')
labelEncoder = joblib.load(dir / 'encoders/crp_label_encoder.pkl')
ANN = tf.keras.models.load_model(dir / "models/crpann.keras")
app = Flask(__name__)

def make_prediction(Na, P, temp, humidity, PH):
    try:
        x = np.array([Na, P, temp, humidity, PH])
        x = x.reshape(1, 5)
        x = scaler.transform(x)
        return labelEncoder.inverse_transform([np.argmax(ANN.predict(x))])[0]
    except Exception as ex:
        print(ex)
        return ex

@app.route('/api/predict', methods=['POST'])
def index():
    try:
        P = float(request.form['phosphorus'])
        N = float(request.form['nitrogen'])
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        PH = float(request.form['PH'])
        crop = make_prediction(N, P, temp, humidity, PH)
        if not crop:
            raise Exception("Something went wrong")
        return crop
    except Exception as ex:
        print(ex)
        return "Something went wrong"

if __name__ == '__main__':
    app.run(debug=True)