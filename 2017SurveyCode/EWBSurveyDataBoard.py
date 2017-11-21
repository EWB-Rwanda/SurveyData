
# coding: utf-8

# In[5]:

#imports for math and data visualization
import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt


# In[6]:

path="2017EWBBoard.csv"
data = pd.read_csv(path)
#changing it to an array, since I'm more familiar with arrays
data=np.array(data)


# In[4]:

'''Looking at just the data from question 1, everyone answered e to the first two questions
The first question asked:
Compared to before the rainwater catchment system was built, 
how has the installation of a rainwater catchment system changed the amount of free time available?
a was much less, d was a little more, and e was much more'''
Q1=[item[0] for item in data]

for item in data:
    if(item[0]=='a'):
        print("a- ",item[4])
    elif(item[0]=='d'):
        print("d- ", item[4])
    elif(item[0]=="e"):
        print("e- ", item[4])

numAnswer=[]
numAnswer.append(Q1.count("a"))
numAnswer.append(Q1.count("d"))
numAnswer.append(Q1.count("e"))

answers=("a","d","e")

y_pos = np.arange(len(answers))

#Bar chart of answers
plt.bar(y_pos,numAnswer, align='center', alpha=0.5)
plt.xticks(y_pos, answers)
plt.title("Question1")
plt.show()


# In[ ]:



