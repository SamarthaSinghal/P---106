import csv
import numpy as np 
import plotly.express as px
coffee = []
sleep = []
with open ("data4.csv") as f :
    df = csv.DictReader(f)
    for i in df :
        coffee.append(float(i["Marks In Percentage"]))
        sleep.append(float(i["Days Present"]))
correlation = np.corrcoef(coffee,sleep)
print(correlation)