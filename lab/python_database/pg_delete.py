#!/usr/bin/python

import psycopg2

try:
    connection = psycopg2.connect(database="pivot_db", 
                                  user="postgres", 
                                  password="Needajob1", 
                                  host="database-1-postgres.ctjowhpkuywk.us-east-2.rds.amazonaws.com", 
                                  port="5432")

    cursor = connection.cursor()
    
    selectQuery = "SELECT * FROM test_crosstab"
    cursor.execute(selectQuery)
    rows = cursor.fetchall()
    
    print ("--------How enumerate works in Python----------")
    my_list = ['apple', 'banana', 'grapes', 'pear']
    myEnumerate = enumerate(my_list)
    print("myEnumerate =", myEnumerate)
    tupleList = list(myEnumerate)
    print("tupleList =", tupleList)
    print("type(myEnumerate) =", type(myEnumerate))
    for counter, value in myEnumerate:
        print ("counter =", counter, "value =", value)
    
    print ("--------Back to SQL---------------")
    for i, k in enumerate(rows):
        print("{} [ {} \t{} \t{}]".format(i+1, k[0], k[1], k[2]))
        
    print("===============================")
    
    deleteQuery = "delete from test_crosstab where product_name = 'product from Python'"
    cursor.execute(deleteQuery)
    
    selectQuery = "SELECT * FROM test_crosstab"
    cursor.execute(selectQuery)
    rows = cursor.fetchall()
    
    for i, k in enumerate(rows):
        print("{} [ {} \t{} \t{}]".format(i+1, k[0], k[1], k[2]))
   #---------------------------------------------------------------------------     
    menu = str(input("Do you want to commit result in database (Y/N) - ")).upper()
    while menu != "Y" and menu != "N":
        menu = str(input("Do you want to commit result in database (Y/N) - ")).upper()
        
    if menu == 'Y':
        connection.commit()
        print("Connection commited!!!")
    else:
        print("Connection not commited!!!")
        
    #---------------------------------------------------------------------------
    
    print("Table state is:")
        
    for i, k in enumerate(rows):
        print("{} [ {} \t{} \t{}]".format(i+1, k[0], k[1], k[2]))
        
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL ", error)
finally:
    # closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
