import openai
import os
import sys
import dotenv
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
openai.api_key=os.getenv('open_api_key')


def get_openai_response(question):
    response=openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[


            {"role": "system", "content": "You are working as chatgpt."},
            {"role": "user", "content": question}])


    output=response.choices[0].message.content
    return output
    

## initilize our streamlit app

st.set_page_config(page_title='Q&A Demo')
st.header("Open AI Applications")
input = st.text_input("Please ask me a Question")
response=get_openai_response(input)
submit=st.button("submit")

if submit:
    st.subheader("The Response to a question is")
    st.write(response)