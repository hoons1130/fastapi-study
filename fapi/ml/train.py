from pathlib import Path

import joblib
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

ARTIFACT_DIR = Path(__file__).resolve().parent / "artifacts"
MODEL_PATH = ARTIFACT_DIR / "wine_classifier.joblib"

def train_model() -> None:

    # 데이터 불러오기
    wine = load_wine()

    X= wine.data
    y= wine.target

    print("입력 데이터 크기:", X.shape)
    print("정답 데이터 크기:", y.shape)
    print("특성 이름:", wine.feature_names)
    print("분류 대상:", wine.target_names)

    #학습데이터와 테스트 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # 모델 생성
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    #모델학습
    model.fit(X_train, y_train)

    #테스트데이터 예측
    predictions = model.predict(X_test)

    #성능평가
    accuracy = accuracy_score(y_test, predictions)
    print(f"정확도: {accuracy:.4f}")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=wine.target_names,
        )
    )
    # 저장 폴더 생성
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

    #학습된 모델 저장
    joblib.dump(model, MODEL_PATH)

    print(f"모델 저장 완료: {MODEL_PATH}")

if __name__=="__main__":
    train_model()