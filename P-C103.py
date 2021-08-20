import pandas as pd
import plotly.express as py



ln= pd.read_csv('COVID.csv')
chart= py.scatter(ln,x='date',y='cases',color='country',size_max=50,title='COVID GLOBAL CASES')

chart.show()
