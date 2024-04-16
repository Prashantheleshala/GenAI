from openai import OpenAI 
import streamlit as st

f = open("key/openai_key.txt")
key=f.read()

client=OpenAI(api_key=key)

st.snow()
st.title("GenAI App - AI Code Reviewer 💻")

prompt = st.text_area("Submit your Python code here for review:", height=200, placeholder="Paste your Python code here.")

if st.button("Analyse Code") == True:
     with st.spinner('Please wait, analyzing your code...'):
        st.subheader("CODE REVIEW")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant that reviews Python code, analyze the submitted code, identify potential bugs, errors, or areas of improvement. After identifying, give the bug report and fixed code snippet in a text box."},
                {"role": "user", "content": prompt}
            ]
        )
        st.write(response.choices[0].message.content)