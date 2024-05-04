import datetime
import streamlit as st


st.title("My Streamlit App")

with st.sidebar:
    agree = st.checkbox("I agree")
    values = st.slider("Select a range of values",0, 100, (25, 75))
    d = st.date_input("Birthday : ")

col1, col2 = st.columns(2)

with col1:


    

    st.write("Hello world")

    my_btn = st.button("Click")

    if my_btn:
        st.write("Hello")
    else:
        st.write("Bye bye")    

    st.text_input("Firtsname")    
    st.text_input("LastName")


with col2:
    weight = st.number_input("Enter weight(kg): ")
    height = st.number_input("Enter height(cm): ")

    btn_calculate = st.button("Calculate BMI ")

    if btn_calculate:
        bmi = weight / ((height/100)**2)
        st.info(bmi)

        if bmi < 18.5:
            st.write("Thin")
        elif 18.5 < bmi < 25:
            st.write("Handsome")
        elif 25 < bmi < 30:
            st.write("Fat")    
