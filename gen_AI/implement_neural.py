# Implentation of neural network in tensorflow

import pandas as pd 
import numpy as np 
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential



# Create and load the dataset
data = {
    'feature1': [0.1, 0.2, 0.3, 0.4, 0.5],
    'feature2': [0.5, 0.4, 0.3, 0.2, 0.1],
    'label': [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
X = df[['feature1', 'feature2']]
y = df[['label']]

# Create a neural network

model = Sequential()
model.add(Dense(8, input_dim = 2, activation="relu"))
model.add(Dense(2, activation = "sigmoid"))

