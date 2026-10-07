# Imports
import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

cols = ['price', 'year', 'manufacturer', 'model', 'condition', 'cylinders',
        'fuel', 'odometer', 'title_status', 'transmission', 'drive', 'type', 'state']
data = pd.read_csv('C:/VsCodeProjects/Used_Cars/vehicles.csv', usecols=cols)
features = ['kilometer', 'dateCreated']
y =data['price']

print(data.head(50))

#print(data[['price', 'yearOfRegistration', 'powerPS', 'kilometer']].describe())
#print(data['offerType'].value_counts())
#print(data['seller'].value_counts())
#print((data['price'] == 0).sum(), "cars listed at price 0")