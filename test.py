import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='password',
    use_pure = True
)

print(mydb)