import random
import plotly.figure_factory as ff
import statistics
import pandas as pd 
import csv

dataSet  = []
df = pd.read_csv('data.csv')
data = df['temp'].tolist()
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataSet.append(value)
mean = statistics.mean(dataSet)
std_deviation = statistics.stdev(dataSet)

print('mean = ', mean)
print('standard deviation = ', std_deviation)