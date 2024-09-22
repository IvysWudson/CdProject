import sqlite3

def conectar():
    conn = sqlite3.connect("TESte.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS teste(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    valor INTEGER,
                                                    produto TEXT NOT NULL)""")
    conn.commit()
    return conn, cur

def desconecta(conn):
    if conn:
        try:
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Erro ao desconectar{e}")

def inserir():
    conn, cur = conectar()
   
    valor = input("Digite o valor desejado\t")
    produto = input("Digite o valor do produto\t")
    cur.execute("INSERT INTO teste(valor, produto) VALUES  (?,?)",(valor, produto))
    conn.commit()
    desconecta(conn)

def remove():
    conn, cur = conectar()
    del_valor = input("Digite o valor a ser removido!")
    cur.execute("DELETE FROM teste WHERE valor = ?", (del_valor,))
    conn.commit()
    desconecta(conn)


    