import sqlite3


conn = sqlite3.connect("sistema.db")
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Clientes (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)"
)


cursor.execute(
    "INSERT INTO Clientes (nome, email) VALUES (?, ?)",
    ("Ana Silva", "ana@email.com"),
)
cursor.execute(
    "INSERT INTO Clientes (nome, email) VALUES (?, ?)",
    ("Carlos Souza", "carlos@email.com"),
)
conn.commit()


cursor.execute(
    "UPDATE Clientes SET email = ? WHERE nome = ?",
    ("ana.nova@email.com", "Ana Silva"),
)
conn.commit()


cursor.execute("SELECT * FROM Clientes WHERE nome LIKE 'A%'")
print("Clientes com 'A':", cursor.fetchall())

cursor.execute("DELETE FROM Clientes WHERE nome = ?", ("Carlos Souza",))
conn.commit()


cursor.execute("SELECT * FROM Clientes")
print("Banco final:", cursor.fetchall())

conn.close()
