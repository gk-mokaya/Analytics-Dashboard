# importing required libs
import streamlit as st 
import pandas as pd
import plotly.express as px 
import seaborn as sns 
import altair as alt 
from matplotlib import pyplot as plt 
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.metric_cards import style_metric_cards
import os
import streamlit as st
from supabase import create_client, Client



# page configuration
st.set_page_config(page_title="Home", page_icon= "👨‍💻", layout="wide")

st.markdown(""" <h3 style="color:#2200ff; font-size:60px"> AUTOMATED ANALYTICS DASHBOARD  </h3>""", unsafe_allow_html=True)

# sidebar
#logo
st.sidebar.image("static/logod.png")


# Initialize Supabase client
supabase_url = "https://gfxsohsucovpiqwgkups.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdmeHNvaHN1Y292cGlxd2drdXBzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDYzMDk0NDAsImV4cCI6MjA2MTg4NTQ0MH0.mBPkKdqMA_UHHAqYLXFX6h2LcPRlM6is8ePlklTIvXQ"
supabase: Client = create_client(supabase_url, supabase_key)


def sign_up(email, password):
    try:
        user = supabase.auth.sign_up({"email": email, "password": password})
        return user
    except Exception as e:
        st.error(f"Registration failed: {e}")
        return None


def sign_in(email, password):
    try:
        user = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return user
    except Exception as e:
        st.error(f"Login failed: {e}")
        return None


def sign_out():
    try:
        supabase.auth.sign_out()
        st.session_state.user_email = None
        st.rerun()
    except Exception as e:
        st.error(f"Logout failed: {e}")


def main_app(user_email):
    st.markdown(
        """<h3 style="color:#2200ff; font-size:40px"> Login successful...  </h3>""",
        unsafe_allow_html=True
        )
    st.success(f"Welcome, {user_email}! 😊😊")
    

    #######################################################################################
    style_metric_cards(background_color="##000000",border_left_color="#22ff00",border_color="#0f00e8")

    st.metric(label="KSK ANALYTICS", value=f"Data-driven decisions aren't just smarter — they're essential.", delta="Discover insights, drive smarter decisions, and elevate your business with real-time, automated analytics.")
    #######################################################################################

    if st.button("Logout"):
        sign_out()


def auth_screen():
    # st.title("Streamlit and Supabase Auth APP")

    # Ensure session key is initialized
    if "user_email" not in st.session_state:
        st.session_state.user_email = None

    if st.session_state.user_email:
        main_app(st.session_state.user_email)
        return  # Exit auth screen

    option = st.selectbox("Choose an action:", ["Login", "Sign Up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if option == "Sign Up" and st.button("Register"):
        user = sign_up(email, password)
        if user and user.user:
            st.success("Registration successful. Please proceed to Log in")

    if option == "Login" and st.button("Login"):
        user = sign_in(email, password)
        if user and user.user:
            st.session_state.user_email = user.user.email
            st.success(f"Welcome back, {email}!")
            st.rerun()


# Run the auth screen
auth_screen()


