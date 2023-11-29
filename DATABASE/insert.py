import mysql.connector 

db_name = "python_test_db" 

mydbconnection = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    passwd="password" ,
    database = db_name
)

print (mydbconnection) 

mycursor = mydbconnection.cursor() 

sqlquery = """
    INSERT INTO Student(ROLL,NAME)
    VALUES('101','ARPAN CHAKRABORTY')
"""

mycursor.execute(sqlquery)
mydbconnection.commit()