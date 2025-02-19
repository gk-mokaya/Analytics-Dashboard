# importing required libs
import streamlit as st 
import pandas as pd
import plotly.express as px 
import seaborn as sns 
import altair as alt 
from matplotlib import pyplot as plt 
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.metric_cards import style_metric_cards


# page configuration
st.set_page_config(page_title="Descriptive analytics", page_icon= "®️", layout="wide")

st.markdown(""" <h3 style="color:#2200ff; font-size:60px"> REALTIME AUTOMATED REPORTS PAGE  </h3>""", unsafe_allow_html=True)

# sidebar
#logo
st.sidebar.image("static/logod.png")

#######################################################################################
style_metric_cards(background_color="##000000",border_left_color="#22ff00",border_color="#0f00e8")

st.metric(label="REPORTS", value=f"Reports Coming Soon...............", delta="Still under development")
#######################################################################################