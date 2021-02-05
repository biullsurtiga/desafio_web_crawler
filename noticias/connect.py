import mysql.connector
import re
import pandas as pd
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="example",
  database="noticias"
)
mycursor = mydb.cursor()

#df = pd.read_json('notices.json')
#df2 = df.to_csv('notices.csv', index= None)
#print(df.to_string()) 
# result = ""
# p = 1
# file = open("notices_Tecnoblog.txt", "r")
# print(file.readline())
# for linha in file:
#   if result == "":
#       if '"title"' in linha:
#           result = linha
#           res = result.split(":")[p].strip('\n')
#           p=p+1
#           print(res)
mycursor.execute("SELECT * FROM noticias")
myresult = mycursor.fetchall()

df = pd.DataFrame(myresult)

df.plot()

plt.show()
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("CREATE TABLE noticias (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), text VARCHAR(255), link VARCHAR(255))")
#mycursor.execute("SHOW TABLES")

#sql = "INSERT INTO noticias (title, author, text, link) VALUES (%s, %s, %s, %s)"
#val = ("John", "Highway 21", "Vlww teste", "www.google.com")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")

#for x in mycursor:
#  print(x)
#mycursor.execute("CREATE DATABASE teste")
#print(mydb)