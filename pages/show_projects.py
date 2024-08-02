import streamlit as st
import pandas as pd
import streamlit as st
import mysql.connector as conn

connection = conn.connect(
  host="sql12.freesqldatabase.com",
  user = st.secrets["username"],
  password=st.secrets["password"],
  database = "sql12625860"
)

data = pd.read_sql("SELECT * FROM ProjectDetails;",connection)
st.header("Your project details are \n")
st.divider()
st.dataframe(data)
