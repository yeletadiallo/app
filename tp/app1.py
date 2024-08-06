import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [2, 2, 3, 14],
    'second column': [10, 20, 30, 100]
}))