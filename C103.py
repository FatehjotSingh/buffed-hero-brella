import pandas as pd
import plotly.express as py



ln= pd.read_csv('data.csv')
chart= py.scatter(ln,x='Population',y='Per capita',size='Percentage',color='Country',size_max=50,title='percapitaincome?')

chart.show()