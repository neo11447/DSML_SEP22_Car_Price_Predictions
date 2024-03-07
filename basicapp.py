import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.header('Hello to my first app', divider='rainbow')
st.header('Hemanth is :blue[cool] :sunglasses:')
st.write("Square Calculator")

def sqr(num):
  return num*num

number = st.number_input('Insert a number')
st.write('The current number is ', number)
st.write("The result is ", sqr(number))
