import pandas as pd
data=[11,12,13,14,15,16,17,18,19,20,101,102,103,104]
xyz=pd.Series(data,index=['a','b','c','d','e','f','g','h','i','j','k','l','m','n'])
print(xyz)
#now we are using filter by value 
#filter by value means selecting onliy those rows of data that meets a certain condition
print(xyz[xyz<=100])
#this above code will prnt integers whose value is less that 100
print("this will present the data whose value is greater than 100",xyz[xyz>=100])





#Link for accessing my notes
#https://noidainstituteofengtech-my.sharepoint.com/:o:/g/personal/0231csiot076_niet_co_in/IgBwA4aX4aDlQaMGjaFFyjWVAbhRUYBExq0O0DQT_CDUOno?e=5NbgAV

