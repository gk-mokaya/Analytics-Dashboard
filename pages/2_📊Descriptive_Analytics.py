# importing required libs
import streamlit as st 
import pandas as pd
import plotly.express as px 
import seaborn as sns 
import altair as alt 
from matplotlib import pyplot as plt 
from streamlit_extras.dataframe_explorer import dataframe_explorer
import datetime

# Redirect to login if not authenticated
if "user_email" not in st.session_state or st.session_state.user_email is None:
    st.warning("You must be logged in to access this page.")
    st.stop()

# page configuration
st.set_page_config(page_title="Descriptive analytics", page_icon= "📊", layout="wide")

st.markdown(""" <h3 style="color:#2200ff; font-size:60px"> DESCRIPTIVE ANALYTICS  </h3>""", unsafe_allow_html=True)

# loading ksk supermarket dataset
df = pd.read_csv("dataksk.csv")

# Loading css file
with open('.streamlit/style.css') as f:
    st.markdown(f"<style> {f.read()}</style>", unsafe_allow_html=True)

st.write('---')

# sidebar
#logo
st.sidebar.image("static/logod.png")


# datepicker
today = datetime.date.today()
with st.sidebar:
    st.title("Select date range to analyze")
    start_date = st.date_input(label="Choose your start date",  max_value=today)
with st.sidebar:
    end_date = st.date_input(label="Choose your end date",max_value=today)

st.error("Displaying descriptive analysis from date "+str(start_date)+ " to "+ str(end_date))

st.write('---')

# Filtering start_date and end_date
df2 = df[(df["Date"]>=str(start_date)) & (df["Date"]<=str(end_date))]

with st.expander("Expand to apply filters on dataframe"):
    filtered_df = dataframe_explorer(df2, case=False)
    st.dataframe(filtered_df, use_container_width=True)

# plots

st.write('---')

st.title("Sales Performance Analysis")

st.write('---')

# perfomance metrics(min, max, mode)
st.subheader("Data Metrics", divider="rainbow")
from streamlit_extras.metric_cards import style_metric_cards

style_metric_cards(background_color="##000000",border_left_color="#22ff00",border_color="#0f00e8")

col1,col2,col3,col4 = st.columns(4)
col1.metric(label="Total items Sold", value = df2["Quantity"].sum(), delta="Total count of product sold so far")
col2.metric(label="Total Cost of Goods", value = f" KSH.{df2['cogs'].sum():,.2f}", delta= f" Average Cost of Goods: Ksh.{df2['cogs'].mean():,.2f}")
col3.metric(label="Total Gross Income", value = f" KSH.{df2['gross income'].sum():,.2f}", delta= f" Average profit per product: Ksh.{df2['gross income'].mean():,.2f}")
col4.metric(label="Total TAX", value = df2["Tax 5%"].sum(), delta="Total amount tax paid (5% of income)")

st.write('---')

a1, a2, a3 = st.columns(3)
with a1:
    
    st.subheader("Total sales per product line", divider='blue')
    source=pd.DataFrame({
      "Quantity (Ksh)":df2["Quantity"],
      "Product line":df2["Product line"],
    })
    bar_chart = alt.Chart(source).mark_bar().encode(
         x="sum(Quantity (Ksh)):Q",
         y=alt.Y("Product line:N",sort="-x")
    )
    st.altair_chart(bar_chart, use_container_width=True)
    


with a2:
    st.subheader("Total sales per  branch", divider='blue')
    source2=pd.DataFrame({
      "Quantity (Ksh)":df2["Quantity"],
      "Branch":df2["Branch"],
    })
    bar_chart2 = alt.Chart(source2).mark_bar().encode(
         x="sum(Quantity (Ksh)):Q",
         y=alt.Y("Branch:N",sort="-x")
    )
    st.altair_chart(bar_chart2, use_container_width=True)

with a3:
    st.subheader("Total sales per city.", divider='blue')
    source3=pd.DataFrame({
        "Quantity (Ksh)":df2["Quantity"],
        "City":df2["City"],
    })
    bar_chart3 = alt.Chart(source3).mark_bar().encode(
        x="sum(Quantity (Ksh)):Q",
        y=alt.Y("City:N",sort="-x")
    )
    st.altair_chart(bar_chart3, use_container_width=True)

st.write('---')

    # Dot plot 
b1,b2 = st.columns(2)

with b1:
    st.subheader("Ratings as per Customer Type", divider="blue")
    source=df2
    chart=alt.Chart(source).mark_circle().encode(
        x="Total",
        y="Rating",
        color="Branch"
    ).interactive()
    st.altair_chart(chart,theme="streamlit",use_container_width=True)

with b2:
    st.subheader("Product Sales distribution",divider="blue")
    sourceb2 = pd.DataFrame({
        "Product line": df2["Product line"],
        "Unitprice (Ksh)": df2["Unitprice"],
        "Date":df2["Date"]
    })
    bar_chartb2 = alt.Chart(sourceb2).mark_bar().encode(
        x="month(Date):O",
        y="sum(Unitprice (Ksh)):Q",
        color="Product line:N"
    )
    st.altair_chart(bar_chartb2,use_container_width=True)


st.write('---')

c1,c2 = st.columns(2)


with c1:
    st.subheader("Personalize Quantitative data for Scatter Plot", divider="green")
    feature_x = st.selectbox("select X, qualitative data",df2.select_dtypes("number").columns)
    feature_y = st.selectbox("select Y, Quantitative data",df2.select_dtypes("number").columns)

    fig, ax=plt.subplots()
    sns.scatterplot(data=df2, x=feature_x, y=feature_y, hue=df2["Product line"], ax=ax)
    st.pyplot(fig)

with c2:
    st.subheader("Features by Frequency", divider="green")
    feature = st.selectbox("Select only Qualitative Data",df2.select_dtypes("object").columns)
    fig, ax = plt.subplots()
    ax.hist(df2[feature], bins=20)

    ax.set_title(f'Histogram of {feature}')
    ax.set_xlabel(feature)
    ax.set_ylabel('Frequency')
    plt.xticks(rotation=45)
    st.pyplot(fig)

st.write('---')