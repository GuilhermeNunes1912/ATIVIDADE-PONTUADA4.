import os 
os.system("cls || clear")
import csv


class Funcionario:
    """
    Representa um funcionário com nome, CPF, cargo e salário.
    """
    def __init__(self, nome, cpf, cargo, salario):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        """
        Retorna uma representação em string do objeto Funcionario.
        """
        return f"Nome: {self.nome}, CPF: {self.cpf}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"

# Lista global para armazenar os funcionários
funcionarios = []
NOME_ARQUIVO_CSV = 'funcionarios.csv'

def exibir_menu():
    """
    Exibe o menu principal de opções para o usuário.
    """
    print("\n--- Menu Principal DENDÊ TECH ---")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Salvar Dados")
    print("6. Carregar Dados")
    print("7. Sair")
    print("---------------------------------")

def validar_cpf(cpf):
    """
    Valida o formato do CPF (apenas dígitos).
    """
    return cpf.isdigit() and len(cpf) == 11

def validar_salario(salario_str):
    """
    Valida se o salário é um número flutuante positivo.
    """
    try:
        salario = float(salario_str)
        return salario >= 0
    except ValueError:
        return False

def adicionar_funcionario():
    """
    Adiciona um novo funcionário à lista de funcionários.
    Solicita nome, CPF, cargo e salário.
    """
    print("\n--- Cadastrar Novo Funcionário ---")
    nome = input("Digite o nome do funcionário: ").strip()
    
    cpf = input("Digite o CPF do funcionário (apenas números): ").strip()
    while not validar_cpf(cpf):
        print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")
        cpf = input("Digite o CPF do funcionário (apenas números): ").strip()

    # Verifica se o CPF já existe
    if any(func.cpf == cpf for func in funcionarios):
        print(f"Erro: Funcionário com CPF '{cpf}' já cadastrado.")
        return

    cargo = input("Digite o cargo do funcionário: ").strip()
    
    salario_str = input("Digite o salário do funcionário: ").strip()
    while not validar_salario(salario_str):
        print("Salário inválido. Digite um valor numérico positivo.")
        salario_str = input("Digite o salário do funcionário: ").strip()
    salario = float(salario_str)

    novo_funcionario = Funcionario(nome, cpf, cargo, salario)
    funcionarios.append(novo_funcionario)
    print(f"Funcionário '{nome}' cadastrado com sucesso!")

def listar_funcionarios():
    """
    Lista todos os funcionários cadastrados ou busca um funcionário específico por CPF.
    """
    if not funcionarios:
        print("\nNenhum funcionário cadastrado ainda.")
        return

    print("\n--- Listar Funcionários ---")
    opcao_busca = input("Deseja listar todos (T) ou buscar por CPF (C)? ").strip().upper()

    if opcao_busca == 'T':
        if not funcionarios:
            print("Nenhum funcionário cadastrado.")
            return
        for i, func in enumerate(funcionarios):
            print(f"{i+1}. {func}")
    elif opcao_busca == 'C':
        cpf_busca = input("Digite o CPF do funcionário que deseja buscar: ").strip()
        encontrado = False
        for func in funcionarios:
            if func.cpf == cpf_busca:
                print(f"\nFuncionário encontrado:\n{func}")
                encontrado = True
                break
        if not encontrado:
            print(f"Funcionário com CPF '{cpf_busca}' não encontrado.")
    else:
        print("Opção inválida. Retornando ao menu.")

def atualizar_funcionario():
    """
    Atualiza as informações de um funcionário existente.
    Permite atualizar nome, cargo e salário. O CPF é usado como identificador.
    """
    if not funcionarios:
        print("\nNenhum funcionário cadastrado para atualizar.")
        return

    print("\n--- Atualizar Funcionário ---")
    cpf_busca = input("Digite o CPF do funcionário que deseja atualizar: ").strip()
    
    funcionario_encontrado = None
    for func in funcionarios:
        if func.cpf == cpf_busca:
            funcionario_encontrado = func
            break

    if funcionario_encontrado:
        print(f"Funcionário encontrado:\n{funcionario_encontrado}")
        
        while True:
            campo_atualizar = input("Qual campo deseja atualizar (nome, cargo, salario)? Ou 'sair' para cancelar: ").strip().lower()
            
            if campo_atualizar == 'nome':
                novo_nome = input("Digite o novo nome: ").strip()
                funcionario_encontrado.nome = novo_nome
                print("Nome atualizado com sucesso!")
            elif campo_atualizar == 'cargo':
                novo_cargo = input("Digite o novo cargo: ").strip()
                funcionario_encontrado.cargo = novo_cargo
                print("Cargo atualizado com sucesso!")
            elif campo_atualizar == 'salario':
                novo_salario_str = input("Digite o novo salário: ").strip()
                while not validar_salario(novo_salario_str):
                    print("Salário inválido. Digite um valor numérico positivo.")
                    novo_salario_str = input("Digite o novo salário: ").strip()
                funcionario_encontrado.salario = float(novo_salario_str)
                print("Salário atualizado com sucesso!")
            elif campo_atualizar == 'sair':
                print("Atualização cancelada.")
                break
            else:
                print("Campo inválido. Tente novamente.")
            
            continuar = input("Deseja atualizar outro campo deste funcionário? (s/n): ").strip().lower()
            if continuar != 's':
                break
    else:
        print(f"Funcionário com CPF '{cpf_busca}' não encontrado.")

def excluir_funcionario():
    """
    Remove um funcionário da lista de funcionários.
    """
    if not funcionarios:
        print("\nNenhum funcionário cadastrado para excluir.")
        return

    print("\n--- Excluir Funcionário ---")
    cpf_excluir = input("Digite o CPF do funcionário que deseja excluir: ").strip()
    
    funcionario_removido = False
    for i, func in enumerate(funcionarios):
        if func.cpf == cpf_excluir:
            confirmacao = input(f"Tem certeza que deseja excluir o funcionário '{func.nome}' (s/n)? ").strip().lower()
            if confirmacao == 's':
                del funcionarios[i]
                print(f"Funcionário com CPF '{cpf_excluir}' excluído com sucesso!")
                funcionario_removido = True
            else:
                print("Exclusão cancelada.")
            break
    
    if not funcionario_removido:
        print(f"Funcionário com CPF '{cpf_excluir}' não encontrado.")

def salvar_dados(nome_arquivo=NOME_ARQUIVO_CSV):
    """
    Salva os dados da lista de funcionários em um arquivo CSV.
    """
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(['Nome', 'CPF', 'Cargo', 'Salario']) # Cabeçalho
            for func in funcionarios:
                writer.writerow([func.nome, func.cpf, func.cargo, func.salario])
        print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
    except IOError as e:
        print(f"Erro ao salvar os dados: {e}")

def carregar_dados(nome_arquivo=NOME_ARQUIVO_CSV):
    """
    Carrega os dados de um arquivo CSV para a lista de funcionários.
    """
    funcionarios.clear() # Limpa a lista antes de carregar novos dados
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            reader = csv.reader(arquivo_csv)
            next(reader) # Pula o cabeçalho
            for row in reader:
                if len(row) == 4:
                    nome, cpf, cargo, salario_str = row
                    try:
                        salario = float(salario_str)
                        funcionarios.append(Funcionario(nome, cpf, cargo, salario))
                    except ValueError:
                        print(f"Erro ao carregar salário para o funcionário {nome} (CPF: {cpf}). Ignorando.")
                else:
                    print(f"Linha inválida no CSV: {row}. Ignorando.")
        print(f"Dados carregados com sucesso de '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando com lista vazia.")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")

def main():
    """
    Função principal que executa o sistema.
    """
    carregar_dados() # Tenta carregar dados ao iniciar

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            adicionar_funcionario()
        elif opcao == '2':
            listar_funcionarios()
        elif opcao == '3':
            atualizar_funcionario()
        elif opcao == '4':
            excluir_funcionario()
        elif opcao == '5':
            salvar_dados()
        elif opcao == '6':
            carregar_dados()
        elif opcao == '7':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida do menu.")

if __name__ == "__main__":


    main()








