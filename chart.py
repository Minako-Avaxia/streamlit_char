import altair as alt
import pandas as pd
import streamlit as st
from vega_datasets import data

# We use @st.cache_data to keep the dataset in cache
@st.cache_data
def get_data():
    source = data.stocks()
    source = source[source.date.gt("2004-01-01")]
    return source

source = get_data()