import streamlit as st

with st.container(border=True):
    st.header("This is a continer")
    st.write("This is inside the continer.")

st.write("This is outside the continer.")
