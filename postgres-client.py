import psycopg2

db_host = "database-1.c6dtlcyvskvq.eu-west-2.rds.amazonaws.com"
db_name = "glue_db"
db_user = "postgres"
db_pass = "Bl4ckburn!23" 

connection = psycopg2.connect(host = db_host, database = db_name, user = db_user, password = db_pass)
print("Connected to the database")

command = """CREATE TABLE employee_info (
     id bigserial PRIMARY KEY,
     first_name VARCHAR(100),
     last_name VARCHAR(100),
     date_of_birth DATE,
     department_id INT
     )""" 

command3 = """INSERT INTO employee_info (first_name, last_name, department_id)
            VALUES ('Simon','Taylor',10)"""

command2 = "SELECT * FROM employee_info"
try:
    cursor = connection.cursor()
    #cursor.execute("SELECT version()")
    cursor.execute(command2)
    result = cursor.fetchone()
    #db_version = cursor.fetchone()
    print(result)
except (psycopg2.DatabaseError, Exception) as error:
    print(error)
connection.commit()
connection.close()
cursor.close()
