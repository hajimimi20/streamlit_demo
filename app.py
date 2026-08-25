import streamlit as st

st.title("Welcome to my first Streamlit web")

st.write("Hello Streamlit!")

name = st.text_input("Insert your name:")

if name:
    st.write(f"Hi，{name}！")


st.chat_input("Ask a question...")