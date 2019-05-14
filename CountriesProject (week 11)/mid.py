
# coding: utf-8

# In[1]:


#import
import pandas as pd
import matplotlib.pyplot as plt

#create empty lists
FR = []
US = []
LV = []
ES = []
LT = []

#Read data and append to lists
file = open("result.txt", "r")
for i in range(500):
    line = file.readline().rstrip()
    line = float(line)
    if i < 100:
        FR.append(line)
    elif i < 200:
        US.append(line)
    elif i < 300: 
        LV.append(line)
    elif i < 400:
        ES.append(line)
    else:
        LT.append(line)
file.close()

#create dataframe
ex_dict = {
    'France': FR,
    'USA': US,
    'Latvia': LV,
    'Spain': ES,
    'Lithuania': LT
}

#columns name
columns = ['France', 'USA', 'Latvia', 'Spain', 'Lithuania']

#line name
index = [i for i in range(0, 100)]

#display dataframe
df = pd.DataFrame(ex_dict, columns=columns, index=index)
df

#compute average
average = df.mean(axis = 0)

#compute standard deviation
sd = df.std(axis = 0)

#compute variance
var = df.var(axis = 0)

#display
print("Average:")
print(average)
print("\nStandard deviation:")
print(sd)
print("\nVariance:")
print(var)

#histogram
df.hist(bins=100, figsize=(20, 15))

#save histogram
#fig, ax = plt.subplots()
#df.hist(ax=ax);
#plt.savefig("output.png")

#boxplot
df.boxplot(figsize=(10, 15)) 

