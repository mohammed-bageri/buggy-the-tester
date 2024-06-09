import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def find_bug_in_code(system_message, code, coding_language):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[
            {"role": "system", "content": f"{system_message}"},
            {"role": "user", "content": f">>Code: {code}\n\n>>Coding language: {coding_language}"},
        ]
    )
    return response.choices[0].message.content


# User inputs and model parameters
st.sidebar.header("Buggy parameters")
prompt_message = "You are Buggy, my Code Tester and code QA. \
                    Based on my code and my \
                    coding language find any bugs in the program. \
                    Then add the right code in the specified coding language with some advise for \
                    the improvement of code."

system_message = st.sidebar.text_area("System message:",
                                      value=prompt_message, disabled=True)
model_temp = st.sidebar.slider("Temp", step=0.01, min_value=0.0,
                               max_value=2.0,
                               value=1.0)
max_token = st.sidebar.slider("Max Token", step=100, min_value=200,
                              max_value=4000,
                              value=512)

st.sidebar.header("User based input:")
code = st.sidebar.text_area("User Code:",
                             value="print(\"hello world\")")
coding_language = st.sidebar.text_input(
    "Coding Language", value="JavaScript")


# Main page components
st.title("🤖 Buggy the Tester")
response = find_bug_in_code(system_message, code, coding_language)


st.markdown(response)