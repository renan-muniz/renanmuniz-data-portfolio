import os
import json
import pickle 
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from preprocessing import preprocess_input
from pathlib import Path



threshold = 0.3

data_path = Path("../data/test_holdout.csv")
df = pd.read_csv(data_path)

with open("../models/feature_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)

with open("../models/xgb_churn.pkl", "rb") as m:
    model = pickle.load(m)



def evaluate():
    
    #Create X and y
    X = df.drop(columns="Churn")
    y = df['Churn']

    y = y.map({"No": 0, "Yes": 1})
    
    lista = []
    
    # Bucle for, for the rows in X. Transforming it into dict, using the preprocess_input function and then adding into the list
    for idx, row in X.iterrows():
        a = row.to_dict()
        
        pre = preprocess_input(a, feature_columns)
        
        lista.append(pre)
        
    X_processed = pd.concat(lista, ignore_index=True)
    
    y_prob = model.predict_proba(X_processed)[:, 1]
    y_pred = (y_prob >= threshold).astype(float)
    
    
    accuracy = accuracy_score(y, y_pred)
    recall = recall_score(y, y_pred)
    precision = precision_score(y, y_pred)
    f1 = f1_score(y, y_pred)
    auc_roc = roc_auc_score(y, y_prob)
    
    result = {
        "threshold": threshold,
        "accuracy": accuracy,
        "recall": recall,
        "precision": precision,
        "f1": f1,
        "auc-roc": auc_roc,
        "n_samples": len(y)
    }
    
    
    for key, value in result.items():
        print(key,":",  value)
    
    
    with open("../models/metrics_holdout.json", "w") as metrics:
        json.dump(result, metrics, indent= 4)
    
    
    
    return result
    
    
    
if __name__ == "__main__":
    evaluate()