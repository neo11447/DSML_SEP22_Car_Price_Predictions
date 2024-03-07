import streamlit as st
import yfinance as yf
import datetime

txt = st.text_input("Enter the stock")
msft = yf.Ticker(txt)

col1, col2 = st.columns(2)
with col1:
    sd = st.date_input("Start Date", datetime.date(2019, 7, 6))
with col2:
    ed = st.date_input("End Date")


# get all stock info
# msft.info
st.header("Welcome to the Stock Analysis")
# get historical market data
hist = msft.history(period  = "1mo")
st.write(hist)

hist1 = msft.history(period  = "1d",start = sd, end = ed)
st.write(hist1)

st.subheader("Closing Chart")
st.line_chart(hist["Open"])
st.subheader("Closing Chart 1")
st.line_chart(hist1["Open"])