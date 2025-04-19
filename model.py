import sqlite3
from datetime import datetime

def get_connection():
    conn = sqlite3.connect("todo.db")  # Crée ou ouvre le fichier todo.db
    conn.row_factory = sqlite3.Row     # Pour pouvoir accéder aux colonnes par nom
    return conn

#creation de la table de la liste
def tab() :
    conn = get_connection()
    conn.execute(''' CREATE TABLE IF NOT EXISTS list(
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        tache TEXT  UNIQUE NOT NULL,
        description TEXT,
        date  DATETIME,
        compler  BOOLEAN DEFAULT 0 )
    ''')
    conn.commit()
    conn.close()

def update(tache,description): #fonction qui ajoute une liste 
    conn = get_connection()
    date = datetime.now()
    conn.execute("INSERT INTO list(tache, description, date, compler) VALUES (?, ?, ?, ?)" ,(tache, description, date, False, )) 
    conn.commit()
    conn.close()

def modifier(tache, descritpion, id):
    conn = get_connection()
    conn.execute("UPDATE list SET tache= ? AND description = ? WHERE id = ? ", (tache, descritpion, id))
    conn.commit()
    conn.close()
    
def delete(id):  #fonction qui surpime les tache liste
    conn = get_connection()
    conn.execute('''DELETE FROM list WHERE id = ?''',(id,))
    conn.commit()
    conn.close()

def cocher(id):
    conn = get_connection()
    cursor= conn.cursor()
    cursor.execute("SELECT compler FROM list WHERE id = ?", (id,))
    current = cursor.fetchone()[0]

    cursor.execute("UPDATE list SET compler = ? WHERE id = ?", (not current, id))
    conn.commit()
    conn.close()

def afficher_la_liste():
    conn = get_connection()
    cursor = conn.execute('SELECT * FROM list ORDER BY date DESC')
    table = cursor.fetchall()
    conn.close()
    return table


