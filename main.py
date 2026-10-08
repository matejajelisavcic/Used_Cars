import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

cols = ['price', 'year', 'manufacturer', 'model', 'condition', 'cylinders',
        'fuel', 'odometer', 'title_status', 'transmission', 'drive', 'type', 'state']
data = pd.read_csv('C:/VsCodeProjects/Used_Cars/vehicles.csv', usecols=cols)

print(data.describe().round().astype(int))

print("Original data: ", data.shape)

print(data['price'].quantile([0.90, 0.95, 0.99, 0.995, 0.999]))
print((data['price'] > 100000).sum(), "rows above 100k")
print((data['price'].between(1, 999)).sum(), "rows between 1 and 999")

low = data[data['price'].between(1, 999)]
print(low['price'].value_counts().head(10))
print(low[['price', 'year', 'odometer']].describe())

# Cleaning
data = data[data['price'].between(1000, 100000)]
data = data[data['year'].between(1990, 2022)]
data = data[data['odometer'].between(100, 400000)]

data['cylinders'] = pd.to_numeric(data['cylinders'].str.split().str[0], errors='coerce')
data['cylinders'] = data['cylinders'].fillna(data['cylinders'].median())

data = data.dropna(subset=['fuel', 'transmission'])

print("After cleaning:", data.shape)
print(data[['price', 'year', 'odometer']].describe())