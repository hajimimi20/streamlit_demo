import streamlit as st

# Page title
st.title("Welcome to My First Streamlit Web")

st.write("Hello, Streamlit!")

# Name input
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hi, {name}!")


# -------------------------
# Sidebar Menu
# -------------------------

st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "",
    ["Home", "About", "Contact"]
)


# -------------------------
# Page Content
# -------------------------

if menu == "Home":
    st.header("Home")
    st.write("Welcome to the Home page!")

elif menu == "About":
    st.header("About")
    st.write("This is my first Streamlit web application.")
    st.write("I am learning Python, SQL, and Streamlit.")

elif menu == "Contact":
    st.header("Contact")
    st.write("You can contact me at:")
    st.write("hajimidb@gmail.com")


# -------------------------
# Footer
# -------------------------

st.markdown("---")
st.caption("© 2026 My Streamlit App")
