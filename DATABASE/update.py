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
    UPDATE Student 
    SET Name = 'AP' 
    WHERE Name = 'Arpan Chakraborty'
"""

mycursor.execute(sqlquery)
mydbconnection.commit()