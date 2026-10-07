import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

pd.set_option('display.float_format', '{:,.0f}'.format)

cols = ['price', 'year', 'manufacturer', 'model', 'condition', 'cylinders',
        'fuel', 'odometer', 'title_status', 'transmission', 'drive', 'type', 'state']
data = pd.read_csv('C:/VsCodeProjects/Used_Cars/vehicles.csv', usecols=cols)

print(data.describe())

print("Original data: ", data.shape)

# Cleaning

data = data[data['price'].between(1000, 100000)]
data = data[data['year'].between(1990, 2022)]
data = data[data['odometer'].between(100, 400000)]