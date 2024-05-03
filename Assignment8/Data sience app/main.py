import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.header("Data science App")
uploaded_file = st.file_uploader("Upload a csv file 📃", type=["csv"])

if uploaded_file is not None:
    st.success("File uploaded✅")

    data = pd.read_csv("movies.csv")
    data = data.head()
    
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    df = pd.DataFrame([data["Name"], data["First_air_date"], data["Popularity"], data["Vote_average"], data["Vote_count"]])

    st.header("Top movies")
    
    st.dataframe(df)

    st.line_chart(df)
    
    st.bar_chart(df)


else:
    
    st.info("No file is uploaded")    




