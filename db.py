import mysql.connector

def get_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="fraKontraktika",
        password="KontraktikaCO",
        database="flaskBlogProsjekt"
    )
    return connection