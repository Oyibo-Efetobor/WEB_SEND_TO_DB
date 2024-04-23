import psycopg2
import psycopg2.extras #for dict referencing

#auth db
hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = 'password'
port_id = 5432

conn = None
cur= None

#db connection
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    #create database table
    cur.execute('DROP TABLE IF EXISTS employee')#to delete and create new table when re run in the db
    
    create_script = ''' CREATE TABLE IF NOT EXISTS employee(
        id    int PRIMARY KEY,
        name    varchar(40) NOT NULL,
        salary    int,
        dept_id    varchar(30)
    )
    '''
    
    #execute table
    cur.execute(create_script)
    
    
    #add data to table 
    insert_script = 'INSERT INTO employee(id, name, salary, dept_id) VALUES(%s,%s,%s,%s)'
    insert_value = [(1,'James',12000,'D1'), (2,'Angela',23000,'D4'), (3,'Moses',160000,'D8'), (4,'Mary',34870,'D6')]
    
    for record in insert_value:
        cur.execute(insert_script, record)
    
    
    
    #fetch data into python script
    cur.execute('SELECT * FROM EMPLOYEE')
    # for record in cur.fetchall():
    #     print(record)
    
    #lets say we want to get 'name' and 'salary'
    for record in cur.fetchall():
        print(record['name'], record['salary'])
        
    #update data
    update_script = 'UPDATE employee SET salary = salary * 1.5'
    cur.execute(update_script)




    # ------------------------------------------------------------------#
    conn.commit()
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()