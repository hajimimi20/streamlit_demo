import streamlit as st
import pymysql
import pandas as pd



def get_connection():

    return pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="acc_passwd",
        charset="utf8mb4"
    )

def check_user(username, password):

    connection = get_connection()
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


def show_main_screen():

    st.subheader("Welcome to the Main Screen")

    connection = get_connection()

    sql = """
        SELECT id, username
        FROM users
    """

    df = pd.read_sql(sql, connection)

    connection.close()

    st.subheader("Users")
    st.dataframe(df, use_container_width=True)


st.title("Streamlit Login System")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)


if st.button("Login", type="primary"):

    if check_user(username, password):

        st.success("Login successful!")

        show_main_screen()

    else:

        st.error("Invalid username or password")