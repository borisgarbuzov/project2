#!/usr/bin/env python
# coding: utf-8

# In[2]:


import psycopg2

con = psycopg2.connect(
  database="boris_db", 
  user="postgres", 
  password="Needajob1", 
  host="database-1-postgres.ctjowhpkuywk.us-east-2.rds.amazonaws.com", 
  port="5432"
) 
 
print("Database opened successfully")

cur = con.cursor()  
cur.execute(" select * from customers ")

print(dir(cur))

from inspect import ismethod

def call_all(obj, *args, **kwargs):
    print("obj =", obj)
    for name in dir(obj):
        print("name =", name)
        attribute = getattr(obj, name)
        print ("attribute =", attribute)
        if ismethod(attribute):
            print("!!!!!!!!!!!!! is a method !!!!!!!!!!!!!!!!!!!!!!!")
            attribute(*args, **kwargs)

print("\n Before call_all(cur) \n")
call_all(cur)
print("\n After call_all(cur) \n")


for att in dir(cur):
    print (att, ' - ', str(getattr(cur,att)))
    print('-------------------------------')



res = dir(cur)
print(type(res))
print(len(res))

print("----------------------------------------")
  
# rows = cur.fetchall()
# for row in rows:  
#     print("cust_id = ", row[0])
#     print("cust_name = ", row[1])
#     print("cust_address = ", row[2])
#     print("cust_city = ", row[3])
#     print("cust_state = ", row[4])
#     print("cust_zip = ", row[5])
#     print("cust_country = ", row[6])
#     print("cust_contact = ", row[7])
#     print("cust_email = ", row[8])
#     print("--------------------------")

print("Operation done successfully")  
con.close() 

