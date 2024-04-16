import pandas as pd
import numpy as np

data = pd.read_csv('credit card.csv')

#print(data.head())

#print(data.isnull().sum())

#print(data.type.value_counts())


type = data['type'].value_counts()
transactions = type.index
quantity = type.values

import plotly.express as px
figure = px.pie(data, 
             values=quantity, 
             names=transactions,hole = 0.5, 
             title="Distribution of Transaction Type")
figure.show()

