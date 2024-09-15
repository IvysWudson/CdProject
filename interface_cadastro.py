import PySimpleGUI as sg
from PySimpleGUI import theme
import sqlite3
from cadastro import conectar, desconectar
theme("DarkGreen2")


def salvar_dados(values):
    conn, cur = conectar()

    try:
        cur.execute("INSERT INTO desligamentos(nome,cpf,cidade,bairro,endereco, celular, data_entrada,alta) VALUES (?,?,?,?,?,?,?,?)",
                    (values['-NOME-'],
                     values['-CPF-'],
                     values['-CIDADE-'],
                     values['-BAIRRO-'],
                     values['-ENDERECO-'],
                     values['-CELULAR-'],
                     values['-DATA-'],
                     values['-TIPO-']
                     
                     ))
        conn.commit()
        sg.popup("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro: linha 22 {e}")
    finally:
        desconectar(conn)


layout=[
    [sg.Text("Nome")],
    [sg.Input(key='-NOME-')],

    [sg.Text("CPF")],
    [sg.Input(key='-CPF-', size=(14,2))],

    [sg.Text("Cidade"), sg.Text("                         UF")],
    [sg.Input(key='-CIDADE-', size=(20,2)), 
        sg.Input(size=(2,2))],

    [sg.Text("Bairro")],
    [sg.Input(size=(20,2), key='-BAIRRO-')],

    [sg.Text("Endereço")],
    [sg.Input(key='-ENDERECO-')],

    [sg.Text("Celular")],
    [sg.Input(size=(15,2), key='-CELULAR-')],

    [sg.Text('Data de entrada')],
    [sg.Input(key='-DATA-')],

    [sg.Text("Modalidade")],
    [sg.Input(key='-TIPO-')],
    [sg.Button("Salvar",key='-SALVAR-')]


    ]
    

window =sg.Window("Pacientes", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-SALVAR-':
        if values['-NOME-'] and values['-CPF-'] and values['-CIDADE-'] and values['-BAIRRO-'] and values['-BAIRRO-'] and values['-ENDERECO-'] and values['-CELULAR-']:
            salvar_dados(values)
    else:
        sg.popup("Erro de sintaxe")


window.close()
        

        


