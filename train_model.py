import matplotlib as plt
import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from inference import input_fn


pd_Data = input_fn()

pd_Data = pd_Data.dropna(how='any', axis=0)

V_bool = ['HeartDisease', 'Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Diabetic', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer']

for cat in V_bool:
    pd_Data[cat] = np.where(pd_Data[cat] == 'Yes', 1, 0)

for vn in ['BMI', 'PhysicalHealth', 'MentalHealth', 'SleepTime']:
    pd_Data[vn] = (pd_Data[vn] - pd_Data[vn].min()) / (pd_Data[vn].max() - pd_Data[vn].min())

pd_Data_Encoded = pd.get_dummies(pd_Data, columns=['Sex'], drop_first=True)
pd_Data_Encoded = pd.get_dummies(pd_Data_Encoded, columns=['AgeCategory'])
pd_Data_Encoded = pd.get_dummies(pd_Data_Encoded, columns=['GenHealth'])
pd_Data_Encoded = pd.get_dummies(pd_Data_Encoded, columns=['Race'])

X_train, X_test, y_train, y_test = train_test_split(
    pd_Data_Encoded.drop(['HeartDisease'], axis=1),
    pd_Data_Encoded['HeartDisease'], # the target
    test_size = 0.2,
    random_state=42)

X_train.to_csv("X_train.csv")
X_test.to_csv("X_test.csv")
y_train.to_csv("y_train.csv")
y_test.to_csv("y_test.csv")

HD_model = LogisticRegression()

HD_model.fit(X_train, y_train)
y_pred = HD_model.predict(X_test)

pickle.dump(HD_model, open("model.h5", "wb"))