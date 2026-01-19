import pandas as pd
calories={'day 1':1750, 'day 2':2100,'day 3':1100}
zxc=pd.Series(calories)
print(zxc)
print("we are using loc here to find the value with specific index")
print(zxc.loc["day 1"])
print("we are using iloc for accessing the value by index")
print(zxc.iloc[0])
print("Now we will increase the value of day 1 by 500 by the use of loc")
#we will do it by
zxc.loc['day 1']+=500
print("zxc.loc['day 1']+=500   this line will increase the value of day 1 by 500")

print(zxc.loc['day 1'])

print("data set is ",zxc)
#now we are doing filter by value
#Suppose i want the value greater than 2000

print(zxc[zxc>=2000],"this will give me value which are greater than 2000")