import plotly.express as px
import plotly.io as pio
import pandas as pd

df = pd.read_csv("output/part-00000", sep='\t', header=None)

fig = px.bar(df, x=0, y=1, title = "Ques 1 bar graph",labels={"0":"City", "1":"No of conferences"})

pio.write_image(fig,'graph.png',scale=6,width=2000,height=1000)