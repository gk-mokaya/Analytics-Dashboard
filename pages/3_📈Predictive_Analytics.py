# importing required libs
import streamlit as st 
import pandas as pd
import plotly.express as px 
import seaborn as sns 
import altair as alt 
from matplotlib import pyplot as plt 
from streamlit_extras.dataframe_explorer import dataframe_explorer

# page configuration
st.set_page_config(page_title="Descriptive analytics", page_icon= "📈", layout="wide")

st.markdown(""" <h3 style="color:#2200ff; font-size:60px"> REALTIME ONLINE PREDICTIVE ANALYTICS  </h3>""", unsafe_allow_html=True)

# sidebar
#logo
st.sidebar.image("static/logod.png")