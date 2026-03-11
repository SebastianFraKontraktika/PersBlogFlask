from dotenv import load_dotenv, dotenv_values 
import mysql.connector
import os
load_dotenv()

Password = os.getenv("db_password")
db_name = os.getenv("db_name")
username = os.getenv("username")

def get_db():
    connection = mysql.connector.connect(
        host="localhost",
        user=username,
        password=Password,
        database=db_name
    )
    return connection