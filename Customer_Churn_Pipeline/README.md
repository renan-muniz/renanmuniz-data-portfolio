# 📉 Customer Churn Prediction — End-to-End Machine Learning Pipeline

This repository contains a complete machine learning pipeline built to predict **customer churn in a telecom company**, including:

- Data cleaning and preprocessing
- Model training (XGBoost)
- Saving production-ready model artifacts
- A Flask API for real-time predictions
- A Streamlit dashboard that consumes the API

---

## 🚀 Live Demo

- 📊 **Streamlit Dashboard:** https://churn-customer.streamlit.app  
- 🌐 **Flask API (Render):** https://churn-project-rtwh.onrender.com

---

## 🧠 Problem Statement

Customer churn represents a major financial risk for telecom companies.  
The goal of this project is to:

> Predict the probability of churn for each customer and provide tools to analyze results, test real customers, and simulate hypothetical ones.

---

## 🏗️ Project Architecture

                 ┌────────────────────┐
                 │   Raw Data (CSV)   │
                 └──────────┬─────────┘
                            │
                            ▼
                    src/etl.py
                            │
                            ▼
              src/train_model.py (XGBoost)
                            │
                            ▼
    models/xgb_churn.pkl   +   models/feature_columns.pkl
                            │
                            ▼
                  src/app.py (Flask API)
                            │
                            ▼
            streamlit_app.py (Streamlit Dashboard)


---

## 🧩 Main Components

### **ETL & Data Processing**
- `src/etl.py` — loads raw data, cleans values, applies encoding and one-hot encoding.

### **Model Training**
- `src/train_model.py` — trains and saves the XGBoost model:
  - `models/xgb_churn.pkl`
  - `models/feature_columns.pkl`

### **Production Preprocessing**
- `src/preprocessing.py` — contains `preprocess_input()` to transform a single JSON request into a model-ready vector.

### **Model Evaluation**
- `src/evaluate_holdout.py` — evaluates the model on `test_holdout.csv` and stores metrics at:
  - `models/metrics_holdout.json`

### **API Layer**
- `src/app.py` (Flask):
  - `GET /` — health check  
  - `POST /predict` — returns:
    ```json
    {
      "Prediction": 0 or 1,
      "Probability": float,
      "Threshold": 0.3
    }
    ```

### **Dashboard**
- `streamlit_app.py` — interactive web app for:
  - model analysis  
  - real customer predictions  
  - manual churn simulation  

---

## 📊 Model Performance (Holdout Set)

Evaluated on **700 unseen samples (test_holdout.csv)**:

| Metric     | Value |
|------------|--------|
| Threshold  | 0.3 |
| Accuracy   | ~0.65 |
| Recall     | ~0.81 |
| Precision  | ~0.42 |
| F1-score   | ~0.55 |
| ROC-AUC    | ~0.78 |

> The threshold was intentionally lowered to 0.3 to maximize recall, prioritizing capturing customers likely to churn.

---

## 🎛️ Streamlit Dashboard Features

### **1. Overview**
- Load model performance from holdout
- Feature importance visualization
- Churn distribution by:
  - Contract type  
  - Internet service  
  - Payment method  
  - and more

### **2. Test Client**
- Select a real customer from holdout data  
- View all customer details  
- Predict churn and compare with the true label  

### **3. Manual Churn Tester**
- Full interactive form to build a hypothetical customer  
- Real-time prediction using the hosted Flask API  
- Highlights high-risk cases based on the model threshold  

---

## 🛠️ How to Run Locally

### 💾 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
