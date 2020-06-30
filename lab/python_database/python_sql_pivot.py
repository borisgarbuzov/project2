"""
https://www.vertabelo.com/blog/creating-pivot-tables-in-postgresql-using-the-crosstab-function/

"""

import psycopg2

con = psycopg2.connect(
  database="pivot_db", 
  user="postgres", 
  password="Needajob1", 
  host="database-1-postgres.ctjowhpkuywk.us-east-2.rds.amazonaws.com", 
  port="5432"
) 
 
print("Database opened successfully")
cur = con.cursor()  
print("dir(cur) = \n", dir(cur))
myStatusMessage = cur.statusmessage
print("\n myStatusMessage =", myStatusMessage)
cur.execute(" select * from evaluations ")
  
  
rows = cur.fetchall()
print("rows = \n", rows)
'''
for row in rows: 
    print("cust_id = ", row[0])
    print("cust_name = ", row[1])
    print("cust_address = ", row[2])
    print("cust_city = ", row[3])
    print("cust_state = ", row[4])
    print("cust_zip = ", row[5])
    print("cust_country = ", row[6])
    print("cust_contact = ", row[7])
    print("cust_email = ", row[8])
    print("--------------------------")
'''
print("Operation done successfully")  
con.close() 