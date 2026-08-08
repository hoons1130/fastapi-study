from pathlib import Path
import joblib
from sqlalchemy.orm import Session
from models.prediction_log import PredictionLog
from schemas.predict import WinePredictRequest

MODEL_PATH = (Path(__file__).resolve().parent.parent/"ml"/"artifacts"/"wine_classifier.joblib")

model = joblib.load(MODEL_PATH)

CLASS_NAMES = [
    "class_0",
    "class_1",
    "class_2"
]

def predict_wine(request: WinePredictRequest, db: Session):
    features = [[
        request.alcohol,
        request.malic_acid,
        request.ash,
        request.alcalinity_of_ash,
        request.magnesium,
        request.total_phenols,
        request.flavanoids,
        request.nonflavanoid_phenols,
        request.proanthocyanins,
        request.color_intensity,
        request.hue,
        request.od280_od315_of_diluted_wines,
        request.proline,
    ]]

    prediction = model.predict(features)[0]

    probabilities = model.predict_proba(features)[0]
    probability = probabilities[prediction]

    prediction_log = PredictionLog(
    prediction=int(prediction),
    probability=float(probability),
)

    db.add(prediction_log)
    db.commit()

    return {
        "prediction": int(prediction),
        "class_name": CLASS_NAMES[prediction],
        "probability": float(probability)
    }