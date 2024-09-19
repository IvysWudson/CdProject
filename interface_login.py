import PySimpleGUI as sg
from hashlib import sha256
import sqlite3
from PySimpleGUI import theme
theme("DarkGreen3")

def conectar_login():
    conn_login = sqlite3.connect("usuarios.db")
    cur_login = conn_login.cursor()

    cur_login.execute("""CREATE TABLE IF NOT EXISTS login(id INTERGER PRIMARY KEY AUTOINCREMENT,
                                                        usuario TEXT NOT NULL UNIQUE,
                                                        senha TEXT NOT NULL UNIQUE )""")
    return conn_login, cur_login

def desconecta_login(conn_login):
    if conn_login:
        try:
            conn_login.commit()
            conn_login.close()
        except Exception as e:
            print(f"Erro: desconecta_login {e}")

def salvar_cad():
    conn_cad, cur_cad = conectar_login()

    usuario = input("Digite seu usuario")
    senha = input("Digite sua senha")
    senha2 = input("Digite novamente sua senha")
    if senha == senha2:
        senha_hash = sha256(senha.encode('utf-8'))
        senha_hash = senha_hash.hexdigest()

        cur_cad.execute("INSERT INTO usuarios(usuario, senha) VALUES ?, ?", (usuario, senha_hash))
        conn_cad.commit()
        print("Usuario cadastrado!")
        







login_layout = [
    [sg.Text("USUARIO"),sg.Input(key='-LOGIN-', size=(13,2))],
    [sg.Text("SENHA   "),sg.Input(key='-SENHA-', size=(13,2), password_char='*')]
    
]

cad_layout = [
    [sg.Text("USUARIO"),sg.Input(key='-LOGIN-', size=(13,2))],
    [sg.Text("SENHA   "),sg.Input(key='-SENHA-', size=(13,2), password_char='*')]
]



cad_window = sg.Window("LOGIN", login_layout)
cad_window.read()
cad_window.close()