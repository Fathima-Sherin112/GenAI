#  LLaMA 2 Chatbot using Streamlit & Ollama

This project is a simple interactive **AI chatbot** built with **Streamlit** for the user interface and **Ollama** for running a local LLaMA model (TinyLLaMA).  
It allows users to chat with an AI assistant directly from their browser — completely **offline** and **without any API keys**.

---

##  Features
-  Clean and modern chat UI with `st.chat_message()`
-  Local LLM inference using **Ollama**
-  Conversation memory stored using `st.session_state`
-  Fast and lightweight TinyLLaMA model
-  Customizable system prompt for behaviour control

---

##  How It Works
1. The app initializes a chat history when launched.  
2. User input is captured through Streamlit’s `st.chat_input()`.  
3. Messages are sent to the local **TinyLLaMA** model using `ollama.chat()`.  
4. The assistant’s reply is displayed on the UI.  
5. Both user and assistant messages are saved in `session_state`, allowing multi-turn conversation.

---

## 🛠️ Installation

### 1. Install Dependencies

pip install -r requirements.txt
