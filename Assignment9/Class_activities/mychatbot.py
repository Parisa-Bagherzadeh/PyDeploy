import streamlit as st
import sqlite3

new_user = st.text_input("Username")
new_password = st.text_input("Password")


if st.button("SignUp"):
