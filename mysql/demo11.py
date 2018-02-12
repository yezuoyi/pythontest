import sys
import mysql.connector as mc

try:
    connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "root",
                             db = "test")
except mc.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

cursor = connection.cursor()

cursor.execute ("DROP TABLE IF EXISTS employee")

# delete 
#cursor.execute("""DROP TABLE employee;""")

sql_command = """
CREATE TABLE employee ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);"""

cursor.execute(sql_command)

staff_data = [ ("William", "Shakespeare", "m", "1961-10-25"),
               ("Frank", "Schiller", "m", "1955-08-17"),
               ("Jane", "Wall", "f", "1989-03-14"),
               ]
               
for staff, p in enumerate(staff_data):
    format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES ({staff_no}, '{first}', '{last}', '{gender}', '{birthdate}');"""

    sql_command = format_str.format(staff_no=staff, first=p[0], last=p[1], gender=p[2], birthdate = p[3])
    print(sql_command)
    cursor.execute(sql_command)
    
connection.commit()


cursor.close()
connection.close()