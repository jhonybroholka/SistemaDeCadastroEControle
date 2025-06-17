# Sistema de Cadastramento e Controle de Livros

# Dicionário principal onde os livros serão armazenados
livros = {}

#Cria a seção Menu
def menu():
    print("Menu:")
    print("1 - Cadastro")
    print("2 - Consulta")
    print("3 - Empréstimo")
    print("4 - Devolução")
    print("5 - Sair")
    opcao = input("Digite uma opção: ")
    return opcao

#Cria a função de cadastro
def cadastrar_livro():
    while True:
        codigo = input("Digite o Código: ")
        if codigo in livros:
            print("Código já cadastrado! Tente outro.")
            continue
        nome = input("Digite o Nome: ")
        editora = input("Digite a Editora: ")
        ano = input("Digite o Ano: ")

        livros[codigo] = {
            "nome": nome,
            "editora": editora,
            "ano": ano,
            "situacao": "disponível"
        }

        print("Cadastro realizado!")
        print(f'{codigo}: ["{nome}", "{editora}", "{ano}", "Disponível para empréstimo"]')

        repetir = input("Deseja realizar novo cadastro (s/n)? ").lower()
        if repetir != 's':
            break

#Cria a função de consulta
def consultar_livros():
    termo = input("\nBusca (deixe em branco para listar todos): ")
    encontrou = False
    for codigo, dados in livros.items():
        if termo == "" or \
           termo in codigo or \
           termo.lower() in dados["nome"].lower() or \
           termo.lower() in dados["editora"].lower() or \
           termo in dados["ano"] or \
           termo.lower() in dados["situacao"].lower():
            print(f'{codigo}: ["Nome: {dados["nome"]}", "Editora: {dados["editora"]}", "Ano: {dados["ano"]}", "Situação: {dados["situacao"]}"]')
            encontrou = True
    if not encontrou:
        print("Nenhum livro encontrado.")

#Cria a função de emprestar o livro
def emprestar_livro():
    codigo = input("Busca: ")
    if codigo not in livros:
        print("Livro não encontrado.")
        return
    dados = livros[codigo]

    if dados["situacao"] == "emprestado":
        print("Não disponível para empréstimo.")
        return

    continuar = input("Deseja continuar o empréstimo (s/n)? ").lower()
    if continuar == 's':
        livros[codigo]["situacao"] = "emprestado"
        print("Livro emprestado")
        print(f'{codigo}: ["Nome: {dados["nome"]}", "Editora: {dados["editora"]}", " Ano: {dados["ano"]}", "Emprestado"]')
    else:
        print("Empréstimo cancelado.")

        #Cria a função de devolver o livro
def devolver_livro():
    codigo = input("Busca: ")
    if codigo not in livros:
        print("Livro não encontrado.")
        return
    dados = livros[codigo]

    if dados["situacao"] == "emprestado":
        livros[codigo]["situacao"] = "Disponível para empréstimo"
        print("Livro devolvido")
        print(f'{codigo}: ["Nome: {dados["nome"]}", "Editora: {dados["editora"]}", " Ano: {dados["ano"]}", "Disponível para empréstimo"]')
    else:
        print("O empréstimo não foi registrado.")


def main():
    while True:
        opcao = menu()
        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            consultar_livros()
        elif opcao == '3':
            emprestar_livro()
        elif opcao == '4':
            devolver_livro()
        elif opcao == '5':
            print("Programa finalizado!")
            break
        else:
            print("Opção inválida!")

# Inicia o programa
main()
