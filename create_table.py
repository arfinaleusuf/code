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
            CREATE TABLE Student
            (
                Roll VARCHAR(5),
                Name varchar(50)
            )
            """

mycursor.execute(sqlquery)
print("create table succesfully")