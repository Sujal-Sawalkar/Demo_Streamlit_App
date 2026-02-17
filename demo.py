import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit !")
st.write(":streamlit: This is your first streamlit app")
st.text("Let's get started")

name = st.text_input("Enter your name")
if st.button("Greet"):
    st.success(f"Hello, {name}!")

df = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("Navigation")
st.image("https://via.placeholder.com/300",caption="Sample Image")
st.video("https://www.youtube.com/watch?v=VqgUkExPvLY")

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)


st.title (" Text and Markdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, 'Code', [link](https://streamlit.io)")
st.code("for i in ranges(5): print(vedant)" , language = "python")
st.text_input("What is your name")
st.text_area("Write something...")
st.number_input("pick a number", min_value = 0, max_value = 100)
st.slider("Choose a range", 0,100)
st.selectbox("Select a fruit",["Apple","Banana","Mango"])
st.multiselect("Choose toppings",["Cheese","Tomato","Olives"])
st.radio("Pick one", ["option A","Option B"])
st.checkbox("I agree to the terms")


st.checkbox("I agree to the terms and conditions")

if st.button("Click me"):
    st.success("Button clicked!")

if st.checkbox("Show Details"):
    st.info("Here are more details...")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")
    if submitted:
        st.success(f"Logged in as {username}")

# ollama list 
#gemma-2b