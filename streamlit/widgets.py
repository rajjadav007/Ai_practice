import streamlit as st
import pandas as pd

st.title("streamlit text input")

name=st.text_input("enter yout name:")

age=st.slider("selerct your age:",0,100,25)


st.write (f"your age is {age}.")

options = ["python", "java", "c++", "javascript"]
choice = st.selectbox("choose your favorite language:",options)
st.write(f"you selected {choice}.")


if name:
    st.write(f"hello,{name}")


data = {
    "name": ["john", "jane", "jake", "jill"],
    "age": [28,24,35,40],
    "city": ["new york", "los angeles", "chicago", "houston"]
}

df=pd.DataFrame(data)
df.to_csv("match_events.csv")
st.write(df)

uploaded_file=st.file_uploader("choose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)