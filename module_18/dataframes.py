import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [42, 42, 42, 42],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Phoenix']

})

