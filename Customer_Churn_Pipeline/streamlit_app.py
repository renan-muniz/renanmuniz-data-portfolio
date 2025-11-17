import streamlit as st
import pandas as pd
import requests
import json
from pathlib import Path





path = Path("data/test_holdout.csv")
df_holdout = pd.read_csv(path)

with open("models/metrics_holdout.json", "r") as m:
    metrics = json.load(m)
    

    
    
url = "http://127.0.0.1:5000/predict" 


st.set_page_config(page_title="Churn Dashboard", layout="wide")

tab1, tab2, tab3 = st.tabs(['Overview', 'Test Client', 'Manual'])

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
        
    st.subheader("Churn Rate(Holdout)")
    st.bar_chart(df_holdout['Churn'].value_counts(normalize=True))
    
    st.subheader("Churn by Contract Type")
    
    df_holdout['Churn_num'] = df_holdout['Churn'].map({'No': 0, "Yes": 1})
    contract_df = df_holdout.groupby(['Contract'])['Churn_num'].mean()
    st.bar_chart(contract_df)
    
    
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
    for col in df_holdout_3.columns:
        if col == "TotalCharges":
            data_api[col] = st.text_input(label= col)
        elif col == "SeniorCitizen":
            data_api[col] = st.selectbox(label= col, options= df_holdout_3[col].unique())
        elif df_holdout_3[col].dtype == object:
            data_api[col] = st.selectbox(label= col, options= df_holdout_3[col].unique())
        else:
            data_api[col] = st.number_input(label=col)
        
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
            
a = """

    gender = st.selectbox(label="Gender", options= df_holdout['gender'].unique())
    senior_citizen = st.selectbox(label="Senior Citizen (1 = Yes, 0 = No)", options= df_holdout['SeniorCitizen'].unique())
    partner = st.selectbox(label="Partner", options= df_holdout['Partner'].unique())
    dependents = st.selectbox(label="Dependents", options= df_holdout['Dependents'].unique())
    
    
    tenure = st.number_input(label="Write tenure")
    
    phone_service = st.selectbox(label="Phone Service", options= df_holdout['PhoneService'].unique())
    multiple_lines = st.selectbox(label="Multiple Lines", options= df_holdout['MultipleLines'].unique())
    internet_service = st.selectbox(label="Internet Service", options= df_holdout['InternetService'].unique())
    online_security = st.selectbox(label="Online Security", options= df_holdout['OnlineSecurity'].unique())
    online_backup = st.selectbox(label="Online Backup", options= df_holdout['OnlineBackup'].unique())
    device_protection = st.selectbox(label="Device Protection", options= df_holdout['DeviceProtection'].unique())
    tech_support = st.selectbox(label="Tech Support", options= df_holdout['TechSupport'].unique())
    streaming_TV = st.selectbox(label="Streaming TV", options= df_holdout['StreamingTV'].unique())
    streaming_movies = st.selectbox(label="Streaming Movies", options= df_holdout['StreamingMovies'].unique())
    contract = st.selectbox(label="Contract", options= df_holdout['Contract'].unique())
    paperless_billing = st.selectbox(label="Paperless Billing", options= df_holdout['PaperlessBilling'].unique())
    payment_method = st.selectbox(label="Payment Method", options= df_holdout['PaymentMethod'].unique())
    
    
    monthly_charges = st.number_input(label="Write Monthly Charges")
    total_charges = st.number_input(label="Write Total Charges")
     
    
    data_api = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service, 
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,        
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV":  streaming_TV,
        "StreamingMovies": streaming_movies, 
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }
    
    
    
    """
    
    
    