import sqlite3 as db
import uuid

conn = db.connect("TASK5/contacts.db")

NAME_COL = 'NAME'
PHONE_COL = 'PHONE_NUMBER'
EMAIL_COL = 'EMAIL'
ADDRESS_COL = 'ADDRESS'

class MyCostumeException(Exception):
    def __init__(self, message):
        self.message = message

conn.execute(F'''
             CREATE TABLE IF NOT EXISTS contacts(
                 {NAME_COL} TEXT NOT NULL,
                 {PHONE_COL} TEXT PRIMARY KEY NOT NULL,
                 {EMAIL_COL} TEXT,
                 {ADDRESS_COL} TEXT
             )
             ''')

def get_contacts():
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    d = list(cur.fetchall())
    data = []
    for i in d:
        j = list(i)
        j.insert(0,str(uuid.uuid4()))
        data.append(tuple(j))
    print(data)
    cur.close()
    
    return tuple(data)
    
def update_contact(name,contact,old_contact,email=None,address=None):
    cur = conn.cursor()
    
    cur.execute(f"SELECT * FROM contacts WHERE {PHONE_COL} = '{old_contact[2]}'")
    isExists = cur.fetchall()
    
    if isExists:
        cur.execute(f'''
                    UPDATE contacts SET {NAME_COL} = '{name}', {PHONE_COL} = '{contact}' , {EMAIL_COL} = '{email}' , {ADDRESS_COL} = '{address}' WHERE {PHONE_COL} = '{old_contact[2]}'
                    ''')
    else:
        raise MyCostumeException("Contact Not Exists")
    
    conn.commit()
    cur.close()

def delete_contect(old_contact):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM contacts WHERE {PHONE_COL} = '{old_contact[2]}'")
    isExists = cur.fetchall()
    
    if isExists:
        cur.execute(f'''
                    DELETE FROM contacts WHERE {PHONE_COL} = '{old_contact[2]}'
                    ''')
        conn.commit()
    else:
        raise MyCostumeException("Contact Not Exists")
    
    cur.close()

def add_contact(name,contact,email=None,address=None):
    cur = conn.cursor()
    try:
        cur.execute(F'''
                    INSERT INTO contacts VALUES('{name}','{contact}','{email}','{address}')
                    ''')
        conn.commit()
    except db.IntegrityError as e:
        raise MyCostumeException("Phone Number Already Exists!!")
    
    cur.close()
    
    

if __name__ == '__main__':
    for i in range(20):
        add_contact(f"DemoContact {i}",f"{11111111*i}",f"{11111*i}@gmail.com")
    # update_contact("Manav","90",old_contact=('Manav', '90', 'None', 'None'))
    # delete_contect(("Manav","90"))
    get_contacts()