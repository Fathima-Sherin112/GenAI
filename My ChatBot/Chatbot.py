import streamlit as st
import ollama  
# Set the title of the app
st.title("LLaMA 2 Chatbot")

# Initialize chat history
if "messages" not in st.session_state: 
    st.session_state["messages"] = [{"role": "system", "content": "You are a friendly and concise AI chatbot. Respond helpfully to whatever the user says."}]

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] != "system":  # Hide system messages,os it shows us and bot replay only
        st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type your message...") 
if user_input:
    # Append user's message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Get response from LLaMA 2
    response = ollama.chat(model="tinyllama", messages=st.session_state["messages"]) # send to local ai model
    assistant_reply = response["message"]["content"]#it store the replay text

    # Append assistant's response
    st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})
    st.chat_message("assistant").write(assistant_reply)
