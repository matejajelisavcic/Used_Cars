import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

cols = ['price', 'year', 'manufacturer', 'model', 'condition', 'cylinders',
        'fuel', 'odometer', 'title_status', 'transmission', 'drive', 'type', 'state']
data = pd.read_csv('C:/VsCodeProjects/Used_Cars/vehicles.csv', usecols=cols)

print(data.describe().round().astype(int))

print("Original data: ", data.shape)

# Cleaning
data = data[data['price'].between(1000, 100000)]
data = data[data['year'].between(1990, 2022)]
data = data[data['odometer'].between(100, 400000)]

data = data.drop_duplicates(subset=['price', 'year', 'manufacturer', 'model', 'odometer'])

for col in ['manufacturer', 'title_status', 'type', 'condition']:
    data[col] = data[col].fillna('unknown')

data['cylinders'] = pd.to_numeric(data['cylinders'].str.split().str[0], errors='coerce')
data['cylinders'] = data['cylinders'].fillna(data['cylinders'].median())

data = data.dropna(subset=['fuel', 'transmission'])

print("After cleaning:", data.shape)
print(data[['price', 'year', 'odometer']].describe())
print(data.head(5))