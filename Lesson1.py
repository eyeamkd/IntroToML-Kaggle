import pandas as pd 

melboure_housing_file_path = './melb_data.csv' 
melbourne_housing_data = pd.read_csv(melboure_housing_file_path)

print(melbourne_housing_data.describe())