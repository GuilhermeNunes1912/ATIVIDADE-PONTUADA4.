
import os
import csv

os.system("cls" if os.name == "nt" else "clear")

class Funcionario:
    def __init__(self, nome, cpf, cargo, salario):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario

funcionarios = []

def mostrar_menu():
    print("\n--- Dendê Tech ---")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Salvar em CSV")
    print("6. Carregar de CSV")
    print("7. Sair")

def cadastrar():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cargo = input("Cargo: ")
    salario = input("Salário: ")
    funcionarios.append(Funcionario(nome, cpf, cargo, salario))
    print("Funcionário cadastrado!")

def listar():
    if not funcionarios:
        print("Nenhum funcionário cadastrado!")
        return
    for f in funcionarios:
        print(f"{f.nome} | CPF: {f.cpf} | Cargo: {f.cargo} | Salário: R${f.salario}")


def atualizar():
    cpf = input("Digite o CPF do funcionário: ")
    for f in funcionarios:
        if f.cpf == cpf:
            f.nome = input("Novo nome: ")
            f.cargo = input("Novo cargo: ")
            f.salario = input("Novo salário: ")
            print("Funcionário atualizado!")
            return
    print("Funcionário não encontrado.")

def deletar():
    cpf = input("Digite o CPF do funcionário: ")
    for f in funcionarios:
        if f.cpf == cpf:
            funcionarios.remove(f)
            print("Funcionário removido!")
            return
    print("Funcionário não encontrado.")

def salvar_csv():
    with open("funcionarios.csv", "w", newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for f in funcionarios:
            escritor.writerow((f.nome, f.cpf, f.cargo, f.salario))
    print("Dados salvos no arquivo 'funcionarios.csv'.")

def carregar_csv():
    try:
        with open("funcionarios.csv", "r") as arquivo:
            leitor = csv.reader(arquivo)
            funcionarios.clear()
            for linha in leitor:
                nome, cpf, cargo, salario = linha
                funcionarios.append(Funcionario(nome, cpf, cargo, salario))
        print("Dados carregados do arquivo.")
    except FileNotFoundError:
        print("Arquivo 'funcionarios.csv' não encontrado.")

while True:
    mostrar_menu()
    opcao = input("Opção (1-7): ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        deletar()
    elif opcao == "5":
        salvar_csv()
    elif opcao == "6":
        carregar_csv()
    elif opcao == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")