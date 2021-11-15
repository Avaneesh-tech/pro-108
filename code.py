import plotly.figure_factory as ff
import csv
import pandas as pd
import plotly.graph_objects as po 

df = pd.read_csv("data.csv")
data = df["Avg Rating"].tolist()
fig=ff.create_distplot(["Avg Rating"],show_hist=False)
fig.show()
