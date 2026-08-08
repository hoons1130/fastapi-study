from pathlib import Path

import joblib
from sklearn.datasets import load_wine



MODEL_PATH = (Path(__file__).resolve().parent/"artifacts"/"wine_classifier.joblib")

model = joblib.load(MODEL_PATH)

def predict_sample():
    wine = load_wine()

    sample = wine.data[0].reshape(1,-1)

    prediction = model.predict(sample)[0]
    print("예측 클래스:", prediction)
    print("실제 클래스:", wine.target[0])
    print("클래스 이름:", wine.target_names[prediction])

if __name__ == "__main__":
    predict_sample()
