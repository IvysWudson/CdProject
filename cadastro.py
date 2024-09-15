import sqlite3
from colorama import init, Fore, Style
init()

def conectar():
    conn = sqlite3.connect("desligamentos.db")
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS desligamentos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                data_entrada TEXT NOT NULL,
                alta TEXT NOT NULL,
                cpf TEXT NOT NULL,
                endereco TEXT NOT NULL,
                celular TEXT NOT NULL)""")
    return conn, cur

def desconectar(conn):
    
    if conn:
        try:
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Erro: linha 22 {e}")

def salvar():
    conn, cur = conectar()
    
    nome = input("Digite o nome do paciente:\t").upper()
    data_entrada = input("Digite a data de entrada:\t")
    alta = input("Digite qual a modalidade de internação:\t").upper()
    cpf = input("Digite o CPF do paciente:\t")
    endereco = input("Digite o endereço:\t").upper()
    celular = input("Digite o celular:\t")

    cur.execute("INSERT INTO desligamentos(nome,data_entrada,alta,cpf, endereco, celular) VALUES(?,?,?,?,?,?) ",
                (nome,data_entrada,alta,cpf,endereco, celular))
    conn.commit()
    print("Cadastro realizado com sucesso!")
    desconectar(conn)


def pesquisa():
    conn, cur = conectar()
    op = input("""
            DIGITE A OPÇÃO DESEJADA:
            [1]-PROCURAR PELO NOME
            [2]-PROCURAR PELO CPF\t""")


    if op == '1':
        nome = input("Digite o nome que deseja procurar:\t").upper()
        cur.execute("SELECT * FROM desligamentos WHERE nome LIKE ?", ('%' + nome + '%',))
        resultados = cur.fetchall()
    elif op == '2':
        cpf = input("Digite o CPF que deseja buscar:\t")
        cur.execute("SELECT * FROM desligamentos WHERE cpf LIKE ?", ('%' + cpf + '%',))
        resultados = cur.fetchall()
    else:
        print("Opção invalida!")
        return

    

    if resultados:
        print(f"Encontrado(s) {len(resultados)} registro(s)")
        for resultado in resultados:
            print(f"{Fore.RED}NOME: {resultado[1]} \n"
                  f"DATA DE ENTRADA: {resultado[2]}\n"
                  f"MODALIDADE: {resultado[3]}\n"
                  f"CPF: {resultado[4]}\n"
                  f"ENDEREÇO: {resultado[5]}\n"
                  f"CELULAR: {resultado[6]}{Style.RESET_ALL}\n\n")
    else:
        print("Nenhum resultado encontrado!")

    desconectar(conn)



while True:
    print("""
              BEM VINDO     
          [1]-CADASTRAR PACIENTE
          [2]-PESQUISAR PACIENTE
          [3]-SAIR""")
    op = input("Digite a opção desejada: ")

    if op == '1':
        salvar()
    elif op == '2':
        pesquisa()
    elif op =='3':
        print("Saindo...")
        break
    else:
        print("Comando invalido!")

    





        
        




    