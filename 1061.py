import csv
import numpy as np 
import plotly.express as px
with open ("data4.csv") as f :
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Marks In Percentage", y = "Days Present")
    fig.show()