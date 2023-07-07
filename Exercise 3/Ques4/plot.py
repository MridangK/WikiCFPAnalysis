import plotly.express as px
import plotly.io as pio
import pandas as pd

df = pd.read_csv('output/part-00000',sep='\t',header=None)
figure = px.bar(df,x=1,y=1, color=0, barmode="group", height=1000, width=2000, labels={"0": "City", "1": "Year","2":"Number of conference"}, title="Time Series Plot")
#increasing bar width
figure.update_traces(width=0.2)
pio.write_image(figure,'plot.png',scale=6,width=2000, height=1000)