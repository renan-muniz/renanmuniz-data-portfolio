import pandas as pd


# Function created to load data and clean it to use in the train_model function 
def load_and_clean(data_path: str = "../data/train.csv"):
    df = pd.read_csv(data_path)
    
    
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors="coerce")
    df = df.dropna(subset=["TotalCharges"])
    
    
    if "customerID" in df.columns:
        df = df.drop(columns="customerID")
        
        
        
    df_encoded = pd.get_dummies(df, drop_first=True)
    
    X = df_encoded.drop(columns="Churn_Yes")
    y = df_encoded['Churn_Yes']
    
    
    return X, y
if __name__ == "__main__":
    X, y = load_and_clean()
    print("✅ ETL good!")
    print("X Shape:", X.shape)
    print("Target Value Distribution:")
    print(y.value_counts())
