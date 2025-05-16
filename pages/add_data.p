import streamlit as st
import pandas as pd

def add_data():
    # Read csv data file
    df=pd.read_csv('dataksk.csv')
    # Create form
    with st.form("form 1",clear_on_submit=True):
        col1,col2,col3,col4,col5,col6,col7=st.columns(7)

        order_id = col1.number_input(label="OrderID")
        branch = col2.selectbox("Branch",df["Branch"])
        city = col3.selectbox("City",df["City"])
        customer=col4.selectbox("Customer Type",df["Customer type"])
        gender=col5.selectbox("Gender",df["Gender"])
        product_line = col6.selectbox("Product line",df["Product line"])
        quantity=col7.number_input("Quantity")

        col8,col9,col10,col11,col12,col13,col14 = st.columns(7)
        unit_price=col8.number_input("Unit Price")
        date = col9._date_input(label="Date")


        # Submit Button
        btn = st.form_submit_button("Save Data to Excel file", type="primary")

        # Form validation logic
        if btn:
            if product_line=="" or gender=="" or order_id=="" or order_date=="" or branch=="" or city=="" or category=="" or customer=="" or quantity==0.00 or unit_price==0.00:
                st.error("All fields are required")
            return False
        else:
            # Insert data to excell
            df = pd.concat([df,pd.DataFrame.from_records([{
                ''
                ''
                ''
                ''
                ''
                ''
                ''
                ''
                'Tax':float(quantity)*float(unit_price)
            }])])
        
        try:
            df.to_csv("dataksk.csv", index=False)
            st.success("Record has been added successfully")
            return True
        
        except:
            st.warning("Unable to write, Please close Excell file")
            return False
        
    #st.experimental_rerun



add_data()



