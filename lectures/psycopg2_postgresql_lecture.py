import psycopg2   # lib needs to be installed

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgresql12' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # CREATE TABLE store -- this code can be used if a db file is not existing
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgresql12' host='localhost' port='5432'")
    cur = conn.cursor()
    #cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item, quantity, price)) -- to avoid sql injections, pass the parameter.
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price)) #dont use '', just pass the parameter
    conn.commit()
    conn.close()

# insert("Coffee Cup", 10, 5) # remember that the string is between str quotes

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgresql12' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall() # to get all the data
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgresql12' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,)) # Note the comma after the parameter
    conn.commit()
    conn.close()

def update(quantity, price,item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgresql12' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

#update(11, 6, "Water Glass")
update(20, 15, "Apple")
print(view())

#create_table()
#insert('Apple', 10, 15)