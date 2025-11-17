import pandas as pd

def preprocess_input(data, feature_columns):
    df = pd.DataFrame([data])
    
    if "TotalCharges" in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors="coerce")  
        df["TotalCharges"] = df['TotalCharges'].fillna(0)
        
    if "customerID" in df.columns:
        df = df.drop(columns="customerID") 
        
    df_encoded = pd.get_dummies(df, drop_first=True)
    
    df_encoded = df_encoded.reindex(columns=feature_columns, fill_value=0   )
    
    return df_encoded 