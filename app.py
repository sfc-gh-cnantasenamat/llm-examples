import streamlit as st
import talib
import numpy as np

st.title("Hello world!")

c = np.random.randn(100)

# this is the library function
k, d = talib.STOCHRSI(c)


