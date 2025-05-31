import os
import pickle
import pandas as pd
import numpy as np

def input_fn():

    goodfile = False

    while not goodfile:
        sfilename = input("Entrez le nom du fichier de la base de données: ")
        goodfile = True
        if not os.path.exists(sfilename) or sfilename[-4:] != ".csv":
            goodfile = False
            print(f"Le nom du fichier: {sfilename} entré est invalide.")
        else:
            pd_file = pd.read_csv(sfilename)
            col_name = ['BMI', 'PhysicalHealth', 'MentalHealth', 'SleepTime','Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Diabetic', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer','Sex','AgeCategory','GenHealth','Race']
            for c in col_name:
                if c not in pd_file.columns:
                    goodfile = False
            if not goodfile:
                print(f"Le fichier: {sfilename} fournis n'a pas le format requis.")
                print("Il manque une ou des colonne(s)")    

    return pd_file


def predict_fn(pd_Data):

    pd_Data = pd_Data.dropna(how='any', axis=0)

    V_bool = ['Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Diabetic', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer']

    for cat in V_bool:
        pd_Data[cat] = np.where(pd_Data[cat] == 'Yes', 1, 0)

    for vn in ['BMI', 'PhysicalHealth', 'MentalHealth', 'SleepTime']:
        pd_Data[vn] = (pd_Data[vn] - pd_Data[vn].min()) / (pd_Data[vn].max() - pd_Data[vn].min())

    pd_Data_Encoded = pd.get_dummies(pd_Data, columns=['Sex'], drop_first=True)
    pd_Data_Encoded = pd.get_dummies(pd_Data_Encoded, columns=['AgeCategory'])
    pd_Data_Encoded = pd.get_dummies(pd_Data_Encoded, columns=['GenHealth'])
    pd_Data_Encoded = pd.get_dummies(pd_Data_Encoded, columns=['Race'])

    HD_Model = pickle.load(open("model.h5", 'rb'))
    
    
    return pd_Data, HD_Model.predict(pd_Data_Encoded)
        

def output_fn(df_Original, Out_predict):    

    df_Pred_Result = df_Original
    df_Pred_Result['Predict_Heart_Disease'] = Out_predict

    df_Pred_Result.to_csv("HD_Result.csv")

#Afficher.... je sais pas encore quoi faire afficher
    print(df_Pred_Result.head())
    


if __name__ == "__main__":
    df_data = input_fn()

    df_Cleaned, predictions = predict_fn(df_data)

    output_fn(df_Cleaned, predictions)