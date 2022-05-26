import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM test")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)