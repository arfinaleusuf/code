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
            INSERT INTO Student(Roll, Name)
            VALUES('101', 'arfin al eusuf')
            """

mycursor.execute(sqlquery)
mydbconnection.commit()

print("insert table succesfully")