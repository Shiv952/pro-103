import pandas as pd
import plotly.express as px

df = pd.read_csv("C:\Users\shiva\Downloads\Pro-103-main\Pro-103-main")

fig = px.scatter(df, x="date", y="cases", color="country")
fig.show()
