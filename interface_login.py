import PySimpleGUI as sg
import hashlib
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

def salvar_cad(usuario, senha):
    conn_cad, cur_cad = conectar_login()

    senha_hash = hashlib.sha256(senha.encode('utf-8')).hexdigest()

    try:
        cur_cad.execute("INSERT INTO login (usuario, senha) VALUES (?, ?)", (usuario, senha_hash))
        conn_cad.commit()
        sg.popup("Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        sg.popup("Erro: O usuário já existe!")
    except Exception as e:
        sg.popup(f"Erro ao cadastrar: {e}")
    
    desconecta_login(conn_cad)







login_layout = [
    [sg.Text("USUARIO"),sg.Input(key='-LOGIN-', size=(13,2))],
    [sg.Text("SENHA   "),sg.Input(key='-SENHA-', size=(13,2), password_char='*')],
    [sg.Button("Cadastrar novo usuario", key='-CADASTRAR_USER-')]
    
]

cad_layout = [
    [sg.Text("USUARIO"),sg.Input(key='-LOGIN_CAD-', size=(13,2))],
    [sg.Text("SENHA   "),sg.Input(key='-SENHA_CAD-', size=(13,2), password_char='*')],
    [sg.Button("SALVAR", key='-SALVAR-'),sg.Button("VOLTAR",key="-VOLTAR-")]
]



log_window = sg.Window("LOGIN", login_layout)
while True:
    event, value = log_window.read()
    try:
        if event == '-CADASTRAR_USER-':
            log_window.hide()
            cad_window = sg.Window("Cadastro", cad_layout)
            while True:
                events2, values2 = cad_window.read()
                try:
                    if events2 == sg.WINDOW_CLOSED or events2 == '-VOLTAR-':
                        cad_window.close()
                        log_window.un_hide()
                        break
                    if events2 == '-SALVAR-':
                        if values2['-LOGIN_CAD-'] and values2['-SENHA_CAD-']:
                            conn = sqlite3.connect("senhas_user.db")
                            cur = conn.cursor()
                            senha_sem = values2['-LOGIN_CAD-']
                            senha_com = hashlib.sha256(senha_sem.encode()).hexdigest()
                            cur.execute('''CREATE TABLE IF NOT EXISTS senhas(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        user TEXT NOT NULL, 
                                        senha2 TEXT NOT NULL)''')
                            cur.execute("INSERT INTO senhas(user, senha2) VALUES (?,?)", (values2['-LOGIN_CAD-'], 
                                                                                          senha_com ))
                            print("Dados salvos com sucesso!!")
                            conn.commit()
                            conn.close()

                            
                            
                except Exception as e:
                    print(f"Erro linha 74 {e}")
                        
        if event == sg.WINDOW_CLOSED:
                break
        
    except Exception as e:
        print(f"Erro: linha 67 {e}")
    






