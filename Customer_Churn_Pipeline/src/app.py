from flask import request, Flask, jsonify
import pickle
from .preprocessing import preprocess_input
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  
MODELS_DIR = BASE_DIR / "models"

app = Flask(__name__)
app.config['DEBUG'] = True

with open(MODELS_DIR / "feature_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)

with open(MODELS_DIR / "xgb_churn.pkl", "rb") as m:
    model = pickle.load(m)
    
threshold = 0.3

@app.route("/", methods=['GET'])
def main():
    return "ok"

@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json(force=True)

    X = preprocess_input(data, feature_columns)
    
    prob = model.predict_proba(X)[:, 1]
    prob_value = float(prob[0])
    
    if prob_value >= threshold:
        pred = 1
    else:
        pred = 0 

    
    return jsonify({"Prediction": pred,
                    "Probability": prob_value,
                    "Threshold": threshold})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
