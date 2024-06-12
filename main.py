# Passo 1: Inicializando a Classe da Agenda Telefônica
class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}  # Dicionário para armazenar os contatos

    # Passo 2: Adicionar Contatos
    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"O contato '{nome}' já existe.")
        else:
            self.contatos[nome] = telefone
            print(f"Contato '{nome}' adicionado com sucesso.")

    # Passo 3: Remover Contatos
    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato '{nome}' removido com sucesso.")
        else:
            print(f"Contato '{nome}' não encontrado.")

    # Passo 4: Pesquisar Contatos
    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        else:
            print(f"Contato '{nome}' não encontrado.")

    # Passo 5: Listar Contatos
    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")

# Passo 6: Criar o Menu de Opções
def menu():
    agenda = AgendaTelefonica()
    while True:
        print("\nMenu:")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Pesquisar contato")
        print("4 - Listar contatos")
        print("5 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif escolha == '2':
            nome = input("Digite o nome do contato a ser removido: ")
            agenda.remover_contato(nome)
        elif escolha == '3':
            nome = input("Digite o nome do contato a ser pesquisado: ")
            agenda.pesquisar_contato(nome)
        elif escolha == '4':
            agenda.listar_contatos()
        elif escolha == '5':
            print("Obrigado por usar a agenda. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Passo 7: Finalizar o Programa
if __name__ == "__main__":
    menu()
