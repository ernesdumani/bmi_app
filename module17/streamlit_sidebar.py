import streamlit as st

st.sidebar.header("Sidebar")
st.sidebar.write("this is a sidebar")
st.sidebar.selectbox("Choose an option", ["option 1", "option 2", "option 3"])
st.sidebar.radio("Go to", ["Home", "settings"])