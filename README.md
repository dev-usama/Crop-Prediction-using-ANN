## Crop Yield Prediction using ANN (Artificial Neural Network)

### 📌 Project Overview

This backend was used in our Graduation Final Year Project to make predictions in Flutter mobile app.
    
    Task: Crop Prediction

    Technologies: Python, Docker, & Artificial Neural Network (ANN)

    Libraries Used: TensorFlow, Pandas, Numpy, & more.

    Frameworks used: Flask

### 📊 Dataset

    Dataset Name: Crop Recommendation Dataset
    Number of Classes/Crops: 22

    Source Link: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset


### 📈 Performance Results

After training with dropout regularization & Adam optimization algorithm, the model achieved the following performance on the test set:

1. Accuracy: 92%
2. Loss: 0.2

### Usage 
    API is from HuggingFace Free Tier Space so it will take 2 to 3 minutes to wake up
    API: https://dev-usama-ahmed-crop-prediction-backend-ann.hf.space/api/predict
    Only one POST API expecting JSON
    sample data = {
        "phosphorus": 42,
        "nitrogen": 90,
        "temperature": 20.879744,
        "humidity": 82.002744,
        "PH": 8.502985
    }
