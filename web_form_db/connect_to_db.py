
import psycopg2
import psycopg2.extras
import random

#authentication
hostname = 'localhost'
database = 'user_details'
username = 'postgres'
pwd = 'password'
port_id = 5432

conn = None
cur = None


table_value = []
#DATABASE CONNECTION
def move_to_db(name_db, email_db, phone_number_db):
    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
        )
        
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        #create  table in database
        # cur.execute('DROP TABLE IF EXISTS USER_TABLE') #to del and create new table when re-run
        
        create_table = '''CREATE TABLE IF NOT EXISTS USER_TABLE(
            id    int PRIMARY KEY,
            name    varchar(40) NOT NULL,
            email    varchar(40),
            phone_number    varchar(20)    
        )
        '''
        
        #execute table creation
        cur.execute(create_table)
        
        #function to add data to list
        # def addData(name_f, email_f, phone_number_f):
        #     tuple_f = (random.randint(1,10000), name_f, email_f, phone_number_f)
        #     return tuple_f
        
        # #function use
        # table_value.append(addData(name_m,email_m,phone_m))
            
        # add data to table
        table_key = 'INSERT INTO USER_TABLE(id, name, email, phone_number) VALUES (%s,%s,%s,%s)'
        # table_value = [(random.randint(1,10000), 'Angela', 'angelabauer23@gmail.com', 8997897764)]
        
        table_value = [(random.randint(1,10000), name_db, email_db, phone_number_db)]
        
        
        for value in table_value:
            cur.execute(table_key, value)
        
        #execute table data insertion   
        cur.execute('SELECT * FROM USER_TABLE')
        
        
        conn.commit()



    except Exception as error:
        print(error)
        
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

