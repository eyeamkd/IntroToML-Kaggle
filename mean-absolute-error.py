import pandas as pd
from sklearn.tree import DecisionTreeRegressor 
from sklearn.metrics import mean_absolute_error 


#loading data 

melbourne_file_path = './melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)

filtered_melbourne_data = melbourne_data.dropna(axis=0)

y = filtered_melbourne_data.Price

melbourne_data_features = ['Rooms', 'Bathroom','Landsize','BuildingArea', 'YearBuilt','Lattitude','Longtitude']

X = filtered_melbourne_data[melbourne_data_features]

model = DecisionTreeRegressor() 

model.fit(X,y)  

predicted_prices = model.predict(X) 
# predicted prices are the predicted Y values that we get 

mae = mean_absolute_error(y, predicted_prices) 

print("Mean Absolute Error is ", mae);
