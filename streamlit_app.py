import streamlit
streamlit.title("My parents new health diner")
streamlit.header("Breakfast menu")
streamlit.text("🥣 Omega Oats & Blue berries")
streamlit.text("🥗 Kale, Spinach")
streamlit.text("🐔 Boiled eggs")
streamlit.text("🥑🍞 Avacodo toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
