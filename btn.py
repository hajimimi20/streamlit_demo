import streamlit as st

st.title("Streamlit 登入系統")

user = st.text_input("帳號")
passwd = st.text_input("密碼", type="password")

if st.button("登入", type="primary"):
    st.write("你輸入的帳號：", user)
    st.write("你輸入的密碼：", passwd)