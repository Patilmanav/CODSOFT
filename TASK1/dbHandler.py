import sqlite3 as db

conn = db.connect("TO-Do_List.db")

conn.execute('''CREATE TABLE IF NOT EXISTS TO_DO(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    task TEXT,
    isChecked BOOLEAN
    )''')


def clear_data():
    cur = conn.cursor()
    cur.execute("DELETE FROM TO_DO")
    conn.commit()
    cur.execute("VACUUM")
    conn.commit()

def add_data(task,isChecked):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO TO_DO(task,isChecked) VALUES('{task}',{isChecked})")
    print("dbHandler: ",f"INSERT INTO TO_DO(task,isChecked) VALUES('{task}',{isChecked})")
    conn.commit()
    
def remove_data(task):
    cur = conn.cursor()
    cur.execute("DELETE FROM TO_DO WHERE task = ?", (task,))
    conn.commit()

def modify_data(old_task, new_task, new_isChecked):
    cur = conn.cursor()
    cur.execute("UPDATE TO_DO SET task = ?, isChecked = ? WHERE task = ?", (new_task, new_isChecked, old_task))
    conn.commit()
    
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT task, isChecked FROM TO_DO")
    f = cur.fetchall()
    data_list = []
    for i in f:
        data = {
            'text': i[0],
            'isChecked': bool(i[1])
        }
        data_list.append(data)
    return data_list
    
if __name__ == '__main__':
    # remove_data("Dinner")
    # remove_data("Dinner")
    # clear_data()
    # add_data("Lunch",False)
    # modify_data("Dinner","Dinner",True)
    # remove_data("Dinner")
    print(get_data())