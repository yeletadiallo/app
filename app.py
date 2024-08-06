import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [12, 2, 3, 4],
    'second column': [15, 20, 30, 40]
}))