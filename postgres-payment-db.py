import psycopg2

db_host = ""
db_name = "glue_db"
db_user = "postgres"
db_pass = "" 

connection = psycopg2.connect(host = db_host, database = db_name, user = db_user, password = db_pass)
print("Connected to the database")

create_table_command = """CREATE TABLE payment_info (
     unique_id int PRIMARY KEY,
     payment_date DATE,
     amount NUMERIC(7,2),
     currency VARCHAR(3),
     scheme VARCHAR(20),
     cardholder_name VARCHAR(100),
     cardholder_location VARCHAR(100)
     )""" 

insert_row_command = """INSERT INTO payment_info (
        unique_id, payment_date, amount, currency, scheme, cardholder_name, cardholder_location)
        VALUES (1111, '2025-07-23',20.33, 'GBP', 'VISA', 'Alan Waterfield', 'Cumbria')"""

select_command = "SELECT * FROM payment_info"

command3 = """INSERT INTO employee_info (first_name, last_name, department_id)
            VALUES ('Simon','Taylor',10)"""

try:
    cursor = connection.cursor()
    cursor.execute(create_table_command)
    connection.commit()
    cursor.execute(insert_row_command)
    connection.commit()
    cursor.execute(select_command)
    result = cursor.fetchone()
    print(result)
    print(result)
except (psycopg2.DatabaseError, Exception) as error:
    print(error)
connection.close()
cursor.close()