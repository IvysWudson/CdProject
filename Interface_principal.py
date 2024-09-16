import PySimpleGUI as sg
from interface_cadastro import *
import sqlite3

def pesquisar():
    conn, cur = sqlite3.connect()

    resultados = []
    
    if values['-PESQUISAR NOME-']:
        nome = values['-PESQUISAR NOME-'].upper()
        cur.execute("SELECT * FROM desligamentos WHERE nome LIKE ?",("%" + nome+"%"))
        resultados = cur.fetchall()
    elif values['-PESQUISAR CPF-']:
        cpf = values ['-PESQUISAR_CPF-'].upper()
        cur.execute("SELECT * FROM delsigamentos WHERE nome LIKE ?",("%"+cpf+"%"))
        resultados = cur.fetchall()


    desconectar(conn)
    return resultados


def janela_pesquisa():
    layout_pesquisa = [
        [sg.Text("Pesquisar por Nome:")],
        [sg.Input(key='-PESQUISAR_NOME-', size=(30,1))],
        [sg.Text("Ou Pesquisar por CPF:")],
        [sg.Input(key='-PESQUISAR_CPF-', size=(30,1))],
        [sg.Button("Pesquisar", key='-PESQUISAR-'), sg.Button("Voltar", key='-VOLTAR-')],
        [sg.Output(size=(60, 10))]  # Para exibir os resultados
    ]
    return sg.Window("Pesquisar Pacientes", layout_pesquisa)

def exibir_resultados(resultados):
    if resultados:
        for resultado in resultados:
            print(f"NOME: {resultado[1]}\n"
                  f"DATA DE ENTRADA: {resultado[2]}\n"
                  f"MODALIDADE: {resultado[3]}\n"
                  f"CPF: {resultado[6]}\n"
                  f"ENDEREÇO: {resultado[7]}\n"
                  f"CELULAR: {resultado[8]}\n"
                  f"---------------------------------\n")
    else:
        print("Nenhum resultado encontrado.")

    







def main():
    # Layout da janela principal
    layout1 = [
        [sg.Button("Cadastrar", key='-CADASTRAR-')],
        [sg.Button("Pesquisar", key='-PESQUISAR-')],
        [sg.Button("Sair", key='-SAIR-')]
    ]

    # Cria a janela principal
    window = sg.Window("Tela Principal", layout1)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == '-SAIR-':
            break
        if event == '-CADASTRAR-':
            window.hide()
            window2 = janela_cadastro()

            while True:
                event2, values2 = window2.read()


                if event2 == sg.WINDOW_CLOSED or event2 == '-VOLTAR-':
                    window2.close()
                    window.un_hide()
                    break
            
                if event2 =='-SALVAR-':
                    if values2['-NOME-'] and values2['-CPF-'] and values2['-CIDADE-'] and values2['-BAIRRO-'] and values2['-ENDERECO-'] and values2['-CELULAR-']:
                        salvar_dados(values2)
                    else:
                        sg.popup("Por favor, preencha todos os campos corretamente.")

                if event2 == '-PESQUISAR-':
                    window2.hide()
                    window3 = janela_pesquisa()

                    while True:
                        event3, values3 = window3.read()
                        
                        if event3 == sg.WINDOW_CLOSED or event3 == '-VOLTAR-':
                            window3.hide()
                            window.un_hide()
                            break
                        if event3 == '-PESQUISAR-':
                            resultados = pesquisar(values3)
                            exibir_resultados(resultados)


    window.close()

main()