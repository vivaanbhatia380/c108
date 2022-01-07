import pandas as pd
import csv 
import plotly.figure_factory as ff

df=pd.read_csv('c108.csv')
heightlist=df['Height(Inches)'].tolist()
weightlist=df['Weight(Pounds)'].tolist()
fig=ff.create_distplot([weightlist],['weight'],show_hist=False)
fig.show()