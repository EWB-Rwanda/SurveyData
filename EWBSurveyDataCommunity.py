
# coding: utf-8

# In[12]:

#imports for math and data visualization
import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt


# In[13]:

#Getting data from csv, Note path will change if running on your local machine
data = pd.read_csv("/Users/shiny/Downloads/2017EWBCommunityMember.csv")
#changing it to an array, since I'm more familiar with arrays
data=np.array(data)


# In[9]:

#Visualizing all data from question 1 in a bar chart
Q1=[item[0] for item in data]
Q1data=[]
Q1Letters=[]
for item in Q1:
    for letter in list(item):
        Q1data.append(ord(letter)-97)
        Q1Letters.append(letter)

#Getting the count of how many answered each thing
numAnswers=[]
numAnswers.append(Q1data.count(0))
numAnswers.append(Q1data.count(1))
numAnswers.append(Q1data.count(2))
numAnswers.append(Q1data.count(3))
numAnswers.append(Q1data.count(4))
numAnswers.append(Q1data.count(5))

answers=("None","Boiling","Clorination","Filtration","Iodine","Other")

y_pos = np.arange(len(answers))

#Bar chart of answers
plt.bar(y_pos,numAnswers, align='center', alpha=0.5)
plt.xticks(y_pos, answers)
plt.title("Question1")
plt.show()


# In[27]:

#Visualizing all data from question 2 in a bar chart
Q2=[item[1] for item in data]
Q2data=[]
Q2Letters=[]
for item in Q2:
    for letter in list(item):
        Q2data.append(ord(letter)-97)
        Q2Letters.append(letter)

#Number of people who answered each for question 2
numAnswers=[]
numAnswers.append(Q2data.count(0))
numAnswers.append(Q2data.count(1))
numAnswers.append(Q2data.count(2))
numAnswers.append(Q2data.count(3))

answers=("Rainwater\n Catchment","Tap Stand","Surface\n Water","Ground Water\n or Well")

y_pos = np.arange(len(answers))


#The bar plot, this should get better labels when we know them
plt.bar(y_pos,numAnswers, align='center', alpha=0.5)
plt.xticks(y_pos, answers)
plt.title("Question2")
plt.show()


# In[32]:

#All data for question 3
#Waiting to confirm whether a,b,c,d,e were actual answers to this question, or whether the question asked from f-j
Q3=[item[2] for item in data]
Q3data=[]
Q3Letters=[]
for item in Q3:
    for letter in list(item):
        Q3data.append(ord(letter)-97)
        Q3Letters.append(letter)


#Number of people who answered each question
numAnswers=[]

numAnswers.append(Q3data.count(5))
numAnswers.append(Q3data.count(6))
numAnswers.append(Q3data.count(7))
numAnswers.append(Q3data.count(8))
numAnswers.append(Q3data.count(9))

answers=("Much\nLess","A Little\nLess","About the\nSame","A Little\nMore","Much\nMore")

y_pos = np.arange(len(answers))


#The bar chart for question 3
plt.bar(y_pos,numAnswers, align='center', alpha=0.5)
plt.xticks(y_pos, answers)
plt.title("Question3")
plt.show()


# In[37]:

#Getting data for question 4
Q4=[item[3] for item in data]
Q4data=[]
Q4Letters=[]
for item in Q4:
    for letter in list(item):
        Q4data.append(ord(letter)-97)
        Q4Letters.append(letter)
print(Q4data)
print(Q4Letters)

#Determining the count of each answer
numAnswers=[]
numAnswers.append(Q4data.count(0))
numAnswers.append(Q4data.count(1))
numAnswers.append(Q4data.count(2))
numAnswers.append(Q4data.count(3))
numAnswers.append(Q4data.count(4))

answers=("Much\nWorse","A Little\nWorse","About the\nSame","A Little\nBetter","Much\nBetter")

y_pos = np.arange(len(answers))


#The bar chart
plt.bar(y_pos,numAnswers, align='center', alpha=0.5)
plt.xticks(y_pos, answers)
plt.title("Question4")
plt.show()


# In[38]:

#Getting data for question 5
Q5=[item[4] for item in data]
Q5data=[]
Q5Letters=[]
for item in Q5:
    for letter in list(item):
        Q5data.append(ord(letter)-97)
        Q5Letters.append(letter)


#Deteriming how many answered what
numAnswers=[]
numAnswers.append(Q5data.count(0))
numAnswers.append(Q5data.count(1))
numAnswers.append(Q5data.count(2))
numAnswers.append(Q5data.count(3))
numAnswers.append(Q5data.count(4))

answers=("Much\nLess","A Little\nLess","About the\nSame","A Little\nMore","Much\nMore")

y_pos = np.arange(len(answers))


#the bar plot
plt.bar(y_pos,numAnswers, align='center', alpha=0.5)
plt.xticks(y_pos, answers)
plt.title("Question5")
plt.show()


# In[113]:

#Getting values for place data
#Note: Did not need to do the for loop since I did not need to split each character as a separate answer
Q6=[item[5] for item in data]

#How many from each place
places=[]
places.append(Q6.count('Nyarutosho'))
places.append(Q6.count('Gasebya'))
places.append(Q6.count('Ntarama'))
places.append(Q6.count('Munini'))


placeNames=['Nyarutosho','Gasebeya','Ntarama','Munini']

y_pos=np.arange(len(placeNames))


#Bar chart
plt.bar(y_pos,places, align='center', alpha=0.5)
plt.xticks(y_pos, placeNames)
plt.title("Question6")
plt.show()

#We apparently have 10 surveys from each site, with the exception of Munini, where we have 11


# In[114]:

'''Things I would like to do:
        Determine answers to each question by site
        Determine what our answers mean
        Maybe look at surveys from last semester and see if anything has changed
        Create some cool visualizations of our data (bar charts are great, but there are some cool data visualization software out there we could try out)
        Anything else?
'''


# In[33]:

'''Setting up the data organized by location.
Counts are just to make sure I was getting the correct number for each place'''
GData=[]
NtData=[]
NyData=[]
MData=[]
Gcount=0
Mcount=0
Nycount=0
Ntcount=0
for x in data:
    if x[5]=="Gasebya":
        Gcount+=1
        GData.append([x[0],x[1],x[2],x[3],x[4],x[5]])
    elif x[5]=="Munini":
        Mcount+=1
        MData.append([x[0],x[1],x[2],x[3],x[4],x[5]])
    elif x[5]=="Ntarama":
        Ntcount+=1
        NtData.append([x[0],x[1],x[2],x[3],x[4],x[5]])
    elif x[5]=="Nyarutosho":
        Nycount+=1
        NyData.append([x[0],x[1],x[2],x[3],x[4],x[5]])
print(Gcount,Mcount,Ntcount,Nycount)


# In[15]:

'''Doing the data analysis again with only Gasebya data'''

#Visualizing all data from question 1 in a bar chart
Q1G=[item[0] for item in GData]
print(Q1G)
Q1data=[]
Q1Letters=[]
for item in Q1G:
    for letter in list(item):
        Q1data.append(ord(letter)-97)
        Q1Letters.append(letter)

print(len(Q1data))
#Getting the count of how many answered each thing
numAnswers=[]
numAnswers.append(Q1data.count(0))
numAnswers.append(Q1data.count(1))
numAnswers.append(Q1data.count(2))
numAnswers.append(Q1data.count(3))
numAnswers.append(Q1data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))

#Bar chart of answers
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="green")
plt.xticks(y_pos, answers)
plt.title("Question1")
plt.show()


#Visualizing all data from question 2 in a bar chart
Q2G=[item[1] for item in GData]
Q2data=[]
Q2Letters=[]
for item in Q2G:
    for letter in list(item):
        Q2data.append(ord(letter)-97)
        Q2Letters.append(letter)

print(Q2G)
#Number of people who answered each for question 2
numAnswers=[]
numAnswers.append(Q2data.count(0))
numAnswers.append(Q2data.count(1))
numAnswers.append(Q2data.count(2))
numAnswers.append(Q2data.count(3))


answers=("a","b","c","d")

y_pos = np.arange(len(answers))


#The bar plot, this should get better labels when we know them
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="green")
plt.xticks(y_pos, answers)
plt.title("Question2")
plt.show()


#All data for question 3
#Waiting to confirm whether a,b,c,d,e were actual answers to this question, or whether the question asked from f-j
Q3G=[item[2] for item in GData]
Q3data=[]
Q3Letters=[]
for item in Q3G:
    for letter in list(item):
        Q3data.append(ord(letter)-97)
        Q3Letters.append(letter)

print(Q3G)
#Number of people who answered each question
numAnswers=[]
numAnswers.append(Q3data.count(0))
numAnswers.append(Q3data.count(1))
numAnswers.append(Q3data.count(2))
numAnswers.append(Q3data.count(3))
numAnswers.append(Q3data.count(4))
numAnswers.append(Q3data.count(5))
numAnswers.append(Q3data.count(6))
numAnswers.append(Q3data.count(7))
numAnswers.append(Q3data.count(8))
numAnswers.append(Q3data.count(9))

answers=("a","b","c","d","e","f","g","h","i","j")

y_pos = np.arange(len(answers))


#The bar chart for question 3
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="green")
plt.xticks(y_pos, answers)
plt.title("Question3")
plt.show()


#Getting data for question 4
Q4G=[item[3] for item in GData]
Q4data=[]
Q4Letters=[]
for item in Q4G:
    for letter in list(item):
        Q4data.append(ord(letter)-97)
        Q4Letters.append(letter)
print(Q4G)


#Determining the count of each answer
numAnswers=[]
numAnswers.append(Q4data.count(0))
numAnswers.append(Q4data.count(1))
numAnswers.append(Q4data.count(2))
numAnswers.append(Q4data.count(3))
numAnswers.append(Q4data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))


#The bar chart
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="green")
plt.xticks(y_pos, answers)
plt.title("Question4")
plt.show()


#Getting data for question 5
Q5G=[item[4] for item in GData]
Q5data=[]
Q5Letters=[]
for item in Q5G:
    for letter in list(item):
        Q5data.append(ord(letter)-97)
        Q5Letters.append(letter)

print(Q5G)
#Deteriming how many answered what
numAnswers=[]
numAnswers.append(Q5data.count(0))
numAnswers.append(Q5data.count(1))
numAnswers.append(Q5data.count(2))
numAnswers.append(Q5data.count(3))
numAnswers.append(Q5data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))


#the bar plot
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="green")
plt.xticks(y_pos, answers)
plt.title("Question5")
plt.show()


# In[16]:

'''Doing the data analysis again with only Munini data'''

#Visualizing all data from question 1 in a bar chart
Q1M=[item[0] for item in MData]
print(Q1M)
Q1data=[]
Q1Letters=[]
for item in Q1M:
    for letter in list(item):
        Q1data.append(ord(letter)-97)
        Q1Letters.append(letter)

print(len(Q1data))
#Getting the count of how many answered each thing
numAnswers=[]
numAnswers.append(Q1data.count(0))
numAnswers.append(Q1data.count(1))
numAnswers.append(Q1data.count(2))
numAnswers.append(Q1data.count(3))
numAnswers.append(Q1data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))

#Bar chart of answers
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="magenta")
plt.xticks(y_pos, answers)
plt.title("Question1")
plt.show()


#Visualizing all data from question 2 in a bar chart
Q2M=[item[1] for item in MData]
Q2data=[]
Q2Letters=[]
for item in Q2M:
    for letter in list(item):
        Q2data.append(ord(letter)-97)
        Q2Letters.append(letter)

print(Q2M)
#Number of people who answered each for question 2
numAnswers=[]
numAnswers.append(Q2data.count(0))
numAnswers.append(Q2data.count(1))
numAnswers.append(Q2data.count(2))
numAnswers.append(Q2data.count(3))


answers=("a","b","c","d")

y_pos = np.arange(len(answers))


#The bar plot, this should get better labels when we know them
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="magenta")
plt.xticks(y_pos, answers)
plt.title("Question2")
plt.show()


#All data for question 3
#Waiting to confirm whether a,b,c,d,e were actual answers to this question, or whether the question asked from f-j
Q3M=[item[2] for item in MData]
Q3data=[]
Q3Letters=[]
for item in Q3M:
    for letter in list(item):
        Q3data.append(ord(letter)-97)
        Q3Letters.append(letter)

print(Q3M)
#Number of people who answered each question
numAnswers=[]
numAnswers.append(Q3data.count(0))
numAnswers.append(Q3data.count(1))
numAnswers.append(Q3data.count(2))
numAnswers.append(Q3data.count(3))
numAnswers.append(Q3data.count(4))
numAnswers.append(Q3data.count(5))
numAnswers.append(Q3data.count(6))
numAnswers.append(Q3data.count(7))
numAnswers.append(Q3data.count(8))
numAnswers.append(Q3data.count(9))

answers=("a","b","c","d","e","f","g","h","i","j")

y_pos = np.arange(len(answers))


#The bar chart for question 3
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="magenta")
plt.xticks(y_pos, answers)
plt.title("Question3")
plt.show()


#Getting data for question 4
Q4M=[item[3] for item in MData]
Q4data=[]
Q4Letters=[]
for item in Q4M:
    for letter in list(item):
        Q4data.append(ord(letter)-97)
        Q4Letters.append(letter)
print(Q4M)


#Determining the count of each answer
numAnswers=[]
numAnswers.append(Q4data.count(0))
numAnswers.append(Q4data.count(1))
numAnswers.append(Q4data.count(2))
numAnswers.append(Q4data.count(3))
numAnswers.append(Q4data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))


#The bar chart
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="magenta")
plt.xticks(y_pos, answers)
plt.title("Question4")
plt.show()


#Getting data for question 5
Q5M=[item[4] for item in MData]
Q5data=[]
Q5Letters=[]
for item in Q5M:
    for letter in list(item):
        Q5data.append(ord(letter)-97)
        Q5Letters.append(letter)

print(Q5M)
#Deteriming how many answered what
numAnswers=[]
numAnswers.append(Q5data.count(0))
numAnswers.append(Q5data.count(1))
numAnswers.append(Q5data.count(2))
numAnswers.append(Q5data.count(3))
numAnswers.append(Q5data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))


#the bar plot
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="magenta")
plt.xticks(y_pos, answers)
plt.title("Question5")
plt.show()


# In[35]:

'''Doing the data analysis again with only Nyarutosho data'''

#Visualizing all data from question 1 in a bar chart
Q1=[item[0] for item in NyData]
print(Q1G)
Q1data=[]
Q1Letters=[]
for item in Q1:
    for letter in list(item):
        Q1data.append(ord(letter)-97)
        Q1Letters.append(letter)

print(len(Q1data))
#Getting the count of how many answered each thing
numAnswers=[]
numAnswers.append(Q1data.count(0))
numAnswers.append(Q1data.count(1))
numAnswers.append(Q1data.count(2))
numAnswers.append(Q1data.count(3))
numAnswers.append(Q1data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))

#Bar chart of answers
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="navy")
plt.xticks(y_pos, answers)
plt.title("Question1")
plt.show()


#Visualizing all data from question 2 in a bar chart
Q2=[item[1] for item in NyData]
Q2data=[]
Q2Letters=[]
for item in Q2:
    for letter in list(item):
        Q2data.append(ord(letter)-97)
        Q2Letters.append(letter)

print(Q2)
#Number of people who answered each for question 2
numAnswers=[]
numAnswers.append(Q2data.count(0))
numAnswers.append(Q2data.count(1))
numAnswers.append(Q2data.count(2))
numAnswers.append(Q2data.count(3))


answers=("a","b","c","d")

y_pos = np.arange(len(answers))


#The bar plot, this should get better labels when we know them
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="navy")
plt.xticks(y_pos, answers)
plt.title("Question2")
plt.show()


#All data for question 3
#Waiting to confirm whether a,b,c,d,e were actual answers to this question, or whether the question asked from f-j
Q3=[item[2] for item in NyData]
Q3data=[]
Q3Letters=[]
for item in Q3:
    for letter in list(item):
        Q3data.append(ord(letter)-97)
        Q3Letters.append(letter)

print(Q3)
#Number of people who answered each question
numAnswers=[]
numAnswers.append(Q3data.count(0))
numAnswers.append(Q3data.count(1))
numAnswers.append(Q3data.count(2))
numAnswers.append(Q3data.count(3))
numAnswers.append(Q3data.count(4))
numAnswers.append(Q3data.count(5))
numAnswers.append(Q3data.count(6))
numAnswers.append(Q3data.count(7))
numAnswers.append(Q3data.count(8))
numAnswers.append(Q3data.count(9))

answers=("a","b","c","d","e","f","g","h","i","j")

y_pos = np.arange(len(answers))


#The bar chart for question 3
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="navy")
plt.xticks(y_pos, answers)
plt.title("Question3")
plt.show()


#Getting data for question 4
Q4=[item[3] for item in NyData]
Q4data=[]
Q4Letters=[]
for item in Q4:
    for letter in list(item):
        Q4data.append(ord(letter)-97)
        Q4Letters.append(letter)
print(Q4)


#Determining the count of each answer
numAnswers=[]
numAnswers.append(Q4data.count(0))
numAnswers.append(Q4data.count(1))
numAnswers.append(Q4data.count(2))
numAnswers.append(Q4data.count(3))
numAnswers.append(Q4data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))


#The bar chart
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="navy")
plt.xticks(y_pos, answers)
plt.title("Question4")
plt.show()


#Getting data for question 5
Q5=[item[4] for item in NyData]
Q5data=[]
Q5Letters=[]
for item in Q5:
    for letter in list(item):
        Q5data.append(ord(letter)-97)
        Q5Letters.append(letter)

print(Q5)
#Deteriming how many answered what
numAnswers=[]
numAnswers.append(Q5data.count(0))
numAnswers.append(Q5data.count(1))
numAnswers.append(Q5data.count(2))
numAnswers.append(Q5data.count(3))
numAnswers.append(Q5data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))


#the bar plot
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="navy")
plt.xticks(y_pos, answers)
plt.title("Question5")
plt.show()


# In[36]:

'''Doing the data analysis again with only Ntarama data'''

#Visualizing all data from question 1 in a bar chart
Q1=[item[0] for item in NtData]
print(Q1G)
Q1data=[]
Q1Letters=[]
for item in Q1:
    for letter in list(item):
        Q1data.append(ord(letter)-97)
        Q1Letters.append(letter)
print(len(Q1data))
#Getting the count of how many answered each thing
numAnswers=[]
numAnswers.append(Q1data.count(0))
numAnswers.append(Q1data.count(1))
numAnswers.append(Q1data.count(2))
numAnswers.append(Q1data.count(3))
numAnswers.append(Q1data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))

#Bar chart of answers
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="navajowhite")
plt.xticks(y_pos, answers)
plt.title("Question1")
plt.show()


#Visualizing all data from question 2 in a bar chart
Q2=[item[1] for item in NtData]
Q2data=[]
Q2Letters=[]
for item in Q2:
    for letter in list(item):
        Q2data.append(ord(letter)-97)
        Q2Letters.append(letter)


print(Q2)
#Number of people who answered each for question 2
numAnswers=[]
numAnswers.append(Q2data.count(0))
numAnswers.append(Q2data.count(1))
numAnswers.append(Q2data.count(2))
numAnswers.append(Q2data.count(3))


answers=("a","b","c","d")

y_pos = np.arange(len(answers))


#The bar plot, this should get better labels when we know them
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="navajowhite")
plt.xticks(y_pos, answers)
plt.title("Question2")
plt.show()


#All data for question 3
#Waiting to confirm whether a,b,c,d,e were actual answers to this question, or whether the question asked from f-j
Q3=[item[2] for item in NtData]
Q3data=[]
Q3Letters=[]
for item in Q3:
    for letter in list(item):
        Q3data.append(ord(letter)-97)
        Q3Letters.append(letter)

print(Q3)
#Number of people who answered each question
numAnswers=[]
numAnswers.append(Q3data.count(0))
numAnswers.append(Q3data.count(1))
numAnswers.append(Q3data.count(2))
numAnswers.append(Q3data.count(3))
numAnswers.append(Q3data.count(4))
numAnswers.append(Q3data.count(5))
numAnswers.append(Q3data.count(6))
numAnswers.append(Q3data.count(7))
numAnswers.append(Q3data.count(8))
numAnswers.append(Q3data.count(9))

answers=("a","b","c","d","e","f","g","h","i","j")

y_pos = np.arange(len(answers))


#The bar chart for question 3
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="navajowhite")
plt.xticks(y_pos, answers)
plt.title("Question3")
plt.show()


#Getting data for question 4
Q4=[item[3] for item in NtData]
Q4data=[]
Q4Letters=[]
for item in Q4:
    for letter in list(item):
        Q4data.append(ord(letter)-97)
        Q4Letters.append(letter)
print(Q4)


#Determining the count of each answer
numAnswers=[]
numAnswers.append(Q4data.count(0))
numAnswers.append(Q4data.count(1))
numAnswers.append(Q4data.count(2))
numAnswers.append(Q4data.count(3))
numAnswers.append(Q4data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))


#The bar chart
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="navajowhite")
plt.xticks(y_pos, answers)
plt.title("Question4")
plt.show()


#Getting data for question 5
Q5=[item[4] for item in NtData]
Q5data=[]
Q5Letters=[]
for item in Q5:
    for letter in list(item):
        Q5data.append(ord(letter)-97)
        Q5Letters.append(letter)

print(Q5)
#Deteriming how many answered what
numAnswers=[]
numAnswers.append(Q5data.count(0))
numAnswers.append(Q5data.count(1))
numAnswers.append(Q5data.count(2))
numAnswers.append(Q5data.count(3))
numAnswers.append(Q5data.count(4))

answers=("a","b","c","d","e")

y_pos = np.arange(len(answers))


#the bar plot
plt.bar(y_pos,numAnswers, align='center', alpha=0.5, color="navajowhite")
plt.xticks(y_pos, answers)
plt.title("Question5")
plt.show()


# In[ ]:



