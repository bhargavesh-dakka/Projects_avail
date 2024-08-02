import streamlit as st
import mysql.connector as conn

connection = conn.connect(
  host="sql12.freesqldatabase.com",
  user = st.secrets["username"],
  password=st.secrets["password"],
  database = "sql12625860"
)


st.header("You have selected Project, Great ! ")
st.divider()
st.subheader("Please enter your deatails below.")
st.divider()

def update_data(name, number):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO ProjectDetails VALUES ('{str(name).capitalize()}','{project_number}')")
    connection.commit()

def check_name(name):
    name = str(name).lower()
    cursor = connection.cursor()
    cursor.execute(f"select name from ProjectDetails;")
    names = []
    for rows in cursor:

        names.append(str(rows[0]).lower())
    
    # st.write(names)
    if name in names:
        return True
    else:
        return False


name = st.text_input("Enter your name")
project_number = st.number_input("Enter your project number")

if st.button("Submit"):
    #popup on success
    if name != "" and project_number != "" :
        if not check_name(name):        
            update_data(str(name).lower(), project_number)
            st.success("Thank you for submitting details.")
            st.write("Have a nice day!")
            
        else:
            st.error("User have already Taken.")

    else:
        st.error("Please enter valid input")


    
