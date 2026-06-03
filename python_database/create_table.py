<<<<<<< HEAD
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sudhakar@505",
    database="hello"
)
cursor=mydb.cursor()
#TABLE IS CREATED
#cursor.execute("CREATE TABLE happy(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30),city VARCHAR(20)")
cursor.execute("SELECT * FROM happy ORDER BY id DESC")
for i  in cursor:
    print(i)
cursor.execute("DELETE FROM happy WHERE id=1")
mydb.commit()
result=cursor.fetchall()
for x in result:
    print(x)
print("new line")
cursor.execute("SELECT * FROM happy limit 3")
for i in cursor:
=======
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sudhakar@505",
    database="hello"
)
cursor=mydb.cursor()
#TABLE IS CREATED
#cursor.execute("CREATE TABLE happy(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30),city VARCHAR(20)")
cursor.execute("SELECT * FROM happy ORDER BY id DESC")
for i  in cursor:
    print(i)
cursor.execute("DELETE FROM happy WHERE id=1")
mydb.commit()
result=cursor.fetchall()
for x in result:
    print(x)
print("new line")
cursor.execute("SELECT * FROM happy limit 3")
for i in cursor:
>>>>>>> efce8ef44b4216f32eb93c37f9e3095654cab697
    print(i)