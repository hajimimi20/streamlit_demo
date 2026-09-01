import streamlit as st

# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="💻",
    layout="wide"
)


# -------------------------
# Global Font & Sidebar CSS
# -------------------------

st.markdown("""
<style>

/* =========================
   Global Font
   ========================= */

html, body, [class*="css"] {
    font-family: "Courier New", Courier, monospace;
}


/* =========================
   Sidebar
   ========================= */

[data-testid="stSidebar"] {
    font-family: "Courier New", Courier, monospace;
}


/* Sidebar title */

[data-testid="stSidebar"] h1 {
    font-family: "Courier New", Courier, monospace;
    font-size: 26px;
    font-weight: bold;
}


/* =========================
   Sidebar Buttons
   ========================= */

[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    border: none;
    border-radius: 10px;

    padding: 12px 15px;
    margin-bottom: 8px;

    background-color: transparent;

    font-family: "Courier New", Courier, monospace;
    font-size: 16px;
    font-weight: bold;

    text-align: left;

    transition: all 0.2s ease;
}


/* Hover effect */

[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #eeeeee;

    transform: translateX(5px);

    border-radius: 10px;
}


/* Button click */

[data-testid="stSidebar"] .stButton > button:active {
    transform: scale(0.98);
}


</style>
""", unsafe_allow_html=True)


# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("Menu")

if "page" not in st.session_state:
    st.session_state.page = "Home"


if st.sidebar.button("🏠  Home"):
    st.session_state.page = "Home"

if st.sidebar.button("📊  Dashboard"):
    st.session_state.page = "Dashboard"

if st.sidebar.button("📁  Data"):
    st.session_state.page = "Data"

if st.sidebar.button("👤  About"):
    st.session_state.page = "About"

if st.sidebar.button("📧  Contact"):
    st.session_state.page = "Contact"


# -------------------------
# Main Content
# -------------------------

if st.session_state.page == "Home":

    st.title("Welcome to My Streamlit Web App")

    st.write("Hello, Streamlit!")

    name = st.text_input("Enter your name:")

    if name:
        st.write(f"Hi, {name}!")


elif st.session_state.page == "Dashboard":

    st.title("📊 Dashboard")

    st.write("Welcome to the Dashboard.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Revenue", "$1.25M")

    with col2:
        st.metric("Stores", "328")

    with col3:
        st.metric("Products", "12,540")


elif st.session_state.page == "Data":

    st.title("📁 Data")

    st.write("This page will display your data.")

    st.dataframe({
        "Product": ["Lipstick", "Foundation", "Mascara"],
        "Sales": [1200, 950, 780]
    })


elif st.session_state.page == "About":

    st.title("👤 About")

    st.write("This is my Streamlit project.")


elif st.session_state.page == "Contact":

    st.title("📧 Contact")

    st.write("Email: hajimidb@gmail.com")


# -------------------------
# Footer
# -------------------------

st.markdown("---")

st.caption("© 2026 My Streamlit App")
