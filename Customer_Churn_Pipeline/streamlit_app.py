import streamlit as st
import pandas as pd
import requests
import json
from pathlib import Path
import pickle



path = Path("data/test_holdout.csv")
df_holdout = pd.read_csv(path)

with open("models/metrics_holdout.json", "r") as m:
    metrics = json.load(m)
    
with open("models/xgb_churn.pkl", "rb") as mod:
    model = pickle.load(mod)
    
with open("models/feature_columns.pkl", "rb") as f:
    feature_col = pickle.load(f)
    
url = "https://churn-project-rtwh.onrender.com/predict"

st.set_page_config(page_title="Churn Dashboard", layout="wide")

tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Test Client', 'Manual', 'Ovewrview'])

with tab1:
    st.header("Model Overview")
    st.write("These metrics come from test_holdout.csv. The threshold used is the same used in the API(0.3).")
    
    col1, col2, col3, = st.columns(3)
    with col1:
        auc_roc = round(metrics['auc-roc'], 2)
        st.metric(label="AUC-ROC", value= auc_roc)
        
    with col2:
        recall = round(metrics['recall'],2)
        st.metric(label="Recall", value= recall)
        
    with col3:
        precision = round(metrics['precision'], 2)
        st.metric(label="Precision", value= precision) 
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        accuracy = round(metrics['accuracy'], 2)
        st.metric(label="Accuracy", value=accuracy)
    with col5:
        f1 = round(metrics['f1'],2)
        st.metric(label= "F1", value= f1)
    
    with col6:
        st.metric(label="Threshold", value=metrics['threshold'])
    
    
    
    col7, col8, col9 = st.columns(3)
    
       
    st.subheader("Churn Rate(Holdout)")
    st.bar_chart(df_holdout['Churn'].value_counts(normalize=True))

    with col7:
        st.subheader("Churn by Contract Type")
        
        df_holdout['Churn_num'] = df_holdout['Churn'].map({'No': 0, "Yes": 1})
        contract_df = df_holdout.groupby(['Contract'])['Churn_num'].mean()
        st.bar_chart(contract_df,  sort='-Churn_num')
    
    with col8:
        st.subheader("Churn by Internet Service")
        internet_serv = df_holdout.groupby(['InternetService'])['Churn_num'].mean()
        st.bar_chart(internet_serv,  sort='-Churn_num')
        
    with col9:
        st.subheader("Churn by Payment Method")
        payment_meth = df_holdout.groupby(['PaymentMethod'])['Churn_num'].mean()
        st.bar_chart(payment_meth, sort='-Churn_num')
        
        
with tab2:
    st.header("Test Client")
    
    select_idx = st.selectbox(label="Choose a test client", options= df_holdout.index)
    
    client_row = df_holdout.loc[select_idx]
    churn_real_text = client_row['Churn']
    churn_real_num =client_row['Churn_num']
    
    st.write(client_row)
    

    if st.button("Predict"):
        
        client_row2 = client_row.copy()
        
        client_row2 = client_row2.drop(['Churn','Churn_num'])
        client_row2 = client_row2.to_dict()
        
        
        response = requests.post(url, json=client_row2)
        data = response.json()

        
        if churn_real_text == "Yes":
            st.write("Real Churn: ", churn_real_text, ", it is a Real Churn")
        else: 
            st.write("Real Churn: ", churn_real_text, ",    it is not Real Churn")

        prediction = data['Prediction']
        probability = round(data['Probability'] * 100, 2)
        threshold = data['Threshold']
        
        
        if prediction == churn_real_num:
            st.success("Real Churn is igual to Prediction!!!")
        else:
            st.error("Real Churn is different to Prediction!!!")
        
        
        
        st.write("Churn Prediction: ", prediction )
        st.write("Probability of Churn: ", probability, "%" )
        if probability >= threshold * 100:
            st.warning("High Churn Risk --- probability above threshold!")
        else:
            st.success("Low Churn Risk --- probability below threshold! ")
        
        st.write("Churn Threshold: ", threshold )




with tab3:
    
    st.header("Manual Churn Tester")
    
    data_api = {}
    df_holdout_3 = df_holdout.drop(columns=['Churn', 'Churn_num', 'customerID'])
    

    
    nice_labels = {
        "gender": 'Gender',
        "SeniorCitizen": 'Senior Citizen',
        "Partner": 'Partner',
        "Dependents": 'Dependents',
        "tenure": 'Tenure',
        "PhoneService": 'Phone Service', 
        "MultipleLines": 'Multiple Lines',
        "InternetService": 'Internet Service',
        "OnlineSecurity": 'Online Security',
        "OnlineBackup": 'Online Backup',        
        "DeviceProtection": 'Device Protection',
        "TechSupport": 'Tech Support',
        "StreamingTV":  'Streaming TV',
        "StreamingMovies": 'Streaming Movies', 
        "Contract": 'Contract',
        "PaperlessBilling": 'Paperless Billing',
        "PaymentMethod": 'Payment Method',
        "MonthlyCharges": 'Monthly Charges',
        "TotalCharges": 'Total Charges'
    }
    
    
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]
    for i, col in enumerate(df_holdout_3.columns):
        
        column_atual = columns[i % 3]
        
        with column_atual:
            if col == "TotalCharges":
                data_api[col] = st.text_input(label= nice_labels.get(col, col))
            elif col == "SeniorCitizen":
                data_api[col] = st.selectbox(label= nice_labels.get(col, col), options= df_holdout_3[col].unique())
            elif df_holdout_3[col].dtype == object:
                data_api[col] = st.selectbox(label= nice_labels.get(col, col), options= df_holdout_3[col].unique())
            else:
                data_api[col] = st.number_input(label=nice_labels.get(col, col))
            
    if st.button("Prediction"):
        response = requests.post(url, json=data_api)
        data_2 = response.json()
        
        prediction = data_2['Prediction']
        probability = round(data_2['Probability'] * 100, 2)
        threshold = data_2['Threshold']

        
        st.write("Churn Prediction: ", prediction )
        st.write("Probability of Churn: ", probability, "%" )
        if probability >= threshold * 100:
            st.warning("High Churn Risk --- probability above threshold!")
        else:
            st.success("Low Churn Risk --- probability below threshold! ")
        
        st.write("Churn Threshold: ", threshold )
            

    
with tab4:
    st.header("Feature Importance Columns")
    
    feature_df = pd.DataFrame(feature_col, columns=['Features'])
    importance = pd.DataFrame(model.feature_importances_, columns=['Importance'])
    feature_importance = pd.concat([feature_df, importance], axis=1)
    feature_importance = feature_importance.sort_values(by='Importance', ascending=False).reset_index()
    
    
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(feature_importance)
    with col2:
        st.bar_chart(feature_importance.iloc[:20],x='Features',  y = 'Importance', sort='-Importance', horizontal=True)
    
    