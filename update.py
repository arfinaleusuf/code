import mysql.connector

db_name = 'python_test_db'

mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='password',
    use_pure = True,
    database=db_name
)

mycursor = mydbconnection.cursor()

sqlquery = """
            UPDATE Student
            SET Name = 'arfin'
            WHERE Name = 'arfin al eusuf'
            """

mycursor.execute(sqlquery)
mydbconnection.commit()

print("update table succesfully")