import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db") #if no db file yet, this code will create it
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # CREATE TABLE store -- this code can be used if a db file is not existing
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

# insert("Coffee Cup", 10, 5) # remember that the string is between str quotes

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall() # to get all the data
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,)) # Note the comma after the parameter
    conn.commit()
    conn.close()

def update(quantity, price,item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()

update(11, 6, "Water Glass")
# delete("Coffee Cup")
print(view())