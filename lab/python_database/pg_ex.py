#!/usr/bin/python

import psycopg2

try:
    connection = psycopg2.connect(database="pivot_db", 
                                  user="postgres", 
                                  password="Needajob1", 
                                  host="database-1-postgres.ctjowhpkuywk.us-east-2.rds.amazonaws.com", 
                                  port="5432")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print("\n Before connection.get_dsn_parameters():")
    print ( connection.get_dsn_parameters(),"\n")
    print("\n After connection.get_dsn_parameters():")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    myQuery =  """
    SELECT *
    FROM CROSSTAB
    (
        'SELECT Product_Name, Product_Category, Product_Count
        FROM test_crosstab
        ORDER BY 1,2'
    )AS T (Product_Name text, IT INT, ELE INT);
    """
    print("myQuery =\n", myQuery, "\n")
    cursor.execute(myQuery)
    record = cursor.fetchone()
    print("record 1 ", record)    
    record = cursor.fetchone()
    print("record 2 ", record)    
    record = cursor.fetchone()
    print("record 3 ", record)    
    record = cursor.fetchone()
    print("record 4 ", record)    
    record = cursor.fetchone()
    print("record 5 ", record)    
    record = cursor.fetchone()
    print("record 6 ", record)    
    
    
    insertQuery = "insert into test_crosstab values ('product from Python 2', 'category from Python 2', 1)"
    cursor.execute(insertQuery)
    selectQuery = "select * from test_crosstab;"
    cursor.execute(selectQuery)
    records = cursor.fetchall()
    print("select records before commit =\n", records) 
    
    deleteQuery = "delete from test_crosstab where product_name = 'product from Python 2'"
    cursor.execute(deleteQuery)
    records = cursor.fetchall()
    print("Delete query: select records before commit =\n", records) 
    #connection.commit()
    cursor.execute(selectQuery)
    records = cursor.fetchall()
    print("select records after commit =\n", records) 
    
        
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL ", error)
finally:
    # closing database connection.
        if(connection):
            print("connection =", connection)
            print("type(connection) =", type(connection))
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            
if (float('nan')):
    print("true branch");
else:
    print("false branch");
a = float('nan')
print("a =", a)
print("type(a) =", type(a))

