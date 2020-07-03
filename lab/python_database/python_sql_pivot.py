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

# from inspect import ismethod

# def call_all(obj, *args, **kwargs):
#     print("obj =", obj)
#     for name in dir(obj):
#         print("name =", name)
#         attribute = getattr(obj, name)
#         print ("attribute =", attribute)
#         if ismethod(attribute):
#             print("!!!!!!!!!!!!! is a method !!!!!!!!!!!!!!!!!!!!!!!")
#             attribute(*args, **kwargs)

# print("\n Before call_all(cur) \n")
# call_all(cur)
# print("\n After call_all(cur) \n")

#=========================
def call_all(obj, *args, **kwargs):
    for name in dir(obj):
        attribute = getattr(obj, name)
        print("attribute =", attribute)
        print("type(attribute) =", type(attribute))
        
        if 'method' in str(attribute) or name.startswith('__'):
            print('{} - is method'.format(name))
        else:
            print('{} - is field => {}'.format(name, str(attribute)))
        print('-----------------------------------')
    
    print('===================================================================')

call_all(cur)


print("Operation done successfully")  
con.close() 

