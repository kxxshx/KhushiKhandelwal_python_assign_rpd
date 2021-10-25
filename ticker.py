#Importing libraries
import pandas as pd

#Reading csv file
data = pd.read_csv("data.csv")

#Removing the row having value as "veu"
data = data.drop(labels=3 , axis=0)

#Converting dataframe to csv file
data.to_csv("ticker_name.csv" , index=False)