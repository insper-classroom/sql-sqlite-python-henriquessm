import sqlite3
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()




def create_table (name, tuple):
    conn = sqlite3.connect('db/database_alunos.db')
    cursor = conn.cursor()
    cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {name} {tuple};
""")
    conn.commit()


def insert_many(name, list, tuple, inter):
    
    cursor.executemany(f"""
    INSERT INTO {name}{tuple}
    VALUES({inter});
    """, list)
    conn.commit()

def select(table, column, variable, aditional):
    print(column)
    print (f'SELECT * FROM {table} WHERE {column} == {variable} {aditional}')
    cursor.execute(f'SELECT * FROM {table} WHERE {column} == {variable} {aditional}')
    conn.commit()
    print(cursor.fetchall())


def delete (table, column, value):
    cursor.execute(f'DELETE FROM {table} WHERE {column} = {value}')
    cursor.execute(f'SELECT * FROM {table} ')
    conn.commit()
    print(cursor.fetchall())

def update(table, variable, value, condition):
    cursor.execute(f'UPDATE {table} SET {variable} = {value} WHERE {condition}')
    cursor.execute(f'SELECT * FROM {table}')
    conn.commit()
    print(cursor.fetchall())
