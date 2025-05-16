import streamlit as st
import mysql.connector
from mysql.connector import Error

# Function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',            # default XAMPP user
            password='',            # leave blank if no password is set
            database='kskdata',
            port=3307
        )
        if connection.is_connected():
            st.success("Connected to the database!")
            return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

# Example usage
def main():
    st.title("XAMPP MySQL + Streamlit App")

    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        st.write("Tables in your database:", tables)
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
