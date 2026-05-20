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
    x = np.array([Na, P, temp, humidity, PH])
    x = x.reshape(1, 5)
    x = scaler.transform(x)
    return labelEncoder.inverse_transform([np.argmax(ANN.predict(x))])[0]

@app.route('/api/predict', methods=['POST'])
def multiply():
    f2 = float(request.form['phosphorus'])
    f1 = float(request.form['nitrogen'])
    f4 = float(request.form['temperature'])
    f5 = float(request.form['humidity'])
    f6 = float(request.form['PH'])
    crop = make_prediction(f1, f2, f4, f5, f6)
    return crop

if __name__ == '__main__':
    app.run(debug=True)