import streamlit as st

with st.form(key="form", clear_on_submit=True):
    name=st.text_input("Enter your name")
    age=st.text_input("Enter your age")
    email = st.text_input("Enter your email")
    biography=st.text_input("Enter your biography")
    terms = st.text_input("Enter your terms adn conditions")
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.write(f"Name:, {name}")
    st.write(f"Age:, {age}")
    st.write(f"Email:, {email}")
    st.write(f"Biography:, {biography}")
    if terms:
        st.write('You agreed to terms and conditions')
    else:
        st.write('You did not agree to terms and conditions')