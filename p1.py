import pandas as pd;
"""data=[100,101,102,103]
data1=["A","B","C","D"]
data2=[True,False]
#Series is a 1-d labled array which can store any data type
series=pd.Series(data)
series1=pd.Series(data1)
series2=pd.Series(data2)
print(series)
print(series1)
print(series2)"""
data=[100,101,102,103]
#Change the index name by using this fxn
series=pd.Series(data,index=['a','b','c','d'])
print(series)
#accessing elements by index
print(series.loc["b"])#loc =location by label
# we can also access elements by the location of integer which is also known as iloc
#iloc stands for integer location 
#we can access elements by its integer location 
print("we are accessing the 1st element the the above code we changed the indexs as ab,c but we can accesses these elements by iloc")
print(series.iloc[0])   