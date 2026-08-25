import streamlit as st
import pymysql


def show_main_screen():
    st.subheader("Login successful!")
    st.write("Welcome to the main screen.")


def check_user(username, password):

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="acc_passwd",
        charset="utf8mb4"
    )

    cursor = connection.cursor()

    sql = """
        SELECT *
        FROM users
        WHERE username = %s
        AND password = %s
    """

    cursor.execute(sql, (username, password))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result is not None


st.title("Streamlit Login")

username = st.text_input("Username")

password = st.text_input("Password",type="password")

if st.button("Login", type="primary"):

    if check_user(username, password):
        st.success("Login successfully!")
        show_main_screen()

    else:
        st.error("Invalid username or password")


if st.button("Cancel", type="secondary"):
    st.write("Login cancelled.")