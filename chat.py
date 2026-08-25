import streamlit as st

st.header("AI chat bot :3")

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# User input
prompt = st.chat_input("Enter message...")


if prompt:
    # Display user's mes
    st.chat_message("user").write(prompt)

    # Save user's mes
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Generate AI response
    answer = f'You said "{prompt}"'

    # Display AI response
    st.chat_message("assistant").write(answer)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })