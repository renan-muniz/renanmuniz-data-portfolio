from flask import request, Flask, jsonify
import pickle
from preprocessing import preprocess_input



app = Flask(__name__)
app.config['DEBUG'] = True

with open("../models/feature_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)
    
with open("../models/xgb_churn.pkl", "rb") as m:
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
    app.run(debug=True)