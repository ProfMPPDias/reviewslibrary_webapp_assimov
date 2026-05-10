import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("Price Ranger", price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]

df_books

fig = px.bar(df_books["year of publication"].value_counts())
fig.update_layout(width=500, height=500)

fig2 = px.histogram(df_books["book price"])

col, col2 = st.columns(2)

col.plotly_chart(fig, use_container_width=False)
col2.plotly_chart(fig2, use_container_width=False)