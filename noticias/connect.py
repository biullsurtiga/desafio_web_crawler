import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="example"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS noticias")
mycursor.execute("USE noticias")
mycursor.execute("CREATE TABLE IF NOT EXISTS noticias (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), text longtext, link VARCHAR(255), source VARCHAR(255))")