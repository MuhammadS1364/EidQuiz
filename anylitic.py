

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('allData.csv')

print(data.head(70))


#remove the deblicate rows
data.drop_duplicates(inplace=True)

#fill the missing string with 'Unknown'
data.fillna('Unknown', inplace=True)
# print(data.head(10))

#check duplicates in UserEmail column
duplicates = data['UserEmail'].duplicated().sum() 

print(f"Number of duplicate rows in UserEmail column: {duplicates}")

#remove duplicates in UserEmail column
data.drop_duplicates(subset='UserEmail', inplace=True)  
#check duplicates again
duplicates_after = data['UserEmail'].duplicated().sum()

print(f"Number of duplicate rows in UserEmail column after removing duplicates: {duplicates_after}")

#print whole data frame after removing duplicates

print(data.head(70))
print(data.info())
print(data.shape)

data.to_csv('cleaned_data.csv', index=False)