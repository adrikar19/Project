import streamlit as st
from openai import OpenAI

# st.set_page_config(
#     page_title="HR Interview ,page_icon="🤖"
# )
#st.title(":blue[Welcome to HR interview screen]")


# if "messages" in st.session_state:
#     del st.session_state["messages"]

st.title("Euphoria's HTML Connect")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key="OPEN_API_KEY")

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "You are a Mock HTML Technology Interviewer. You need to generate HTML interview questions and validate user's answers. Always ask one question at a time. Always ask one question at a time and if answer is correct ask the next question in the same response. Ask slowly easy to tough questions. If user starts different discussion, bring them back to HTML interview discussion."}]
    st.session_state.messages.append({"role": "assistant", "content": "Hello, welcome to Euphoria, How are you today?"})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if(message["role"] !="system"):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
