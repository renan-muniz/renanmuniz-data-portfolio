from etl import load_and_clean
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
import joblib
import os


X, y = load_and_clean()

# Function created to train the model and save the model and the feature columns
def train():
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    model = XGBClassifier(
    objective='binary:logistic',
    n_estimators=100,
    max_depth=2,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric='logloss',
    scale_pos_weight =2.76
    )

    model.fit(X_train, y_train)
    
    y_prob = model.predict_proba(X_test)[:,1]
    y_pred = (y_prob >= 0.3).astype(float)
    
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("AUC-ROC:", roc_auc_score(y_test, y_prob))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    
    
    
    os.makedirs("../models", exist_ok=True)
    
    
    joblib.dump(model, "../models/xgb_churn.pkl")
    joblib.dump(list(X_train.columns), "../models/feature_columns.pkl")
    print("✅ Model saved in '../models/xgb_churn.pkl'")
    

if __name__ == "__main__":
    print("🚀 Starting model training...")
    train()
    print("✅ Training successfully completed!")
