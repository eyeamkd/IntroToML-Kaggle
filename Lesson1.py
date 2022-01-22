import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melboure_housing_file_path = './melb_data.csv' 
melbourne_housing_data = pd.read_csv(melboure_housing_file_path) 
columns = melbourne_housing_data.columns 

#dropping missing values from the dataset 

melbourne_housing_data_without_na = melbourne_housing_data.dropna(axis=0) 

# we pick a single colum by using a "dot" 

price_data = melbourne_housing_data_without_na.Price 

#using the dot notation to predict the price, which is called prediction target 
# The price is our target, and in order to achieve the target we need input parameters
# The params that drive the price value 

prediction_target_features = ['Rooms', 'Bathroom', 'Landsize','Lattitude','Longtitude'] 

features_data = melbourne_housing_data_without_na[prediction_target_features] 

# using scikit learn to use DecisionTree

melbourne_data_model = DecisionTreeRegressor(random_state=1)

melbourne_data_model.fit(features_data,price_data)

print('Making Predictions for the following Houses..')
print(price_data) 

print("Predictions are")
prediction = melbourne_data_model.predict(features_data.head()) 
print(prediction)