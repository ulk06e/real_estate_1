import streamlit as st 
import AI

st.title("Al Majidiya Residence")

if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "open_ai" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your request..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role" : "user", "content" : prompt})
    
    with st.chat_message("assistant"):
        stream = AI.get_response(model=st.session_state["openai_model"], messages=st.session_state.messages)
        response = st.write_stream(stream)
    st.session_state.messages.append({"role" : "assistant", "content" : response})




