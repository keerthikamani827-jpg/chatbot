import os
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="AI Chat Assistant",
    layout="centered"
)

st.title("AI Chat Assistant")
st.caption("Powered by Hugging Face")

st.markdown(
    """
    <style>
    .stChatMessage {
        border-radius: 15px;
    }

    .main {
        padding-top: 20px;
    }

    h1 {
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input(
    " Ask me anything..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner(" Thinking..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=st.session_state.messages
            )

            answer = response.choices[0].message.content

        st.markdown(answer)

    # Save AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
