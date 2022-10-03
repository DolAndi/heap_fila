
class Menu:
    def __init__(self, titulo, opcoes):
        self.titulo = titulo
        self.opcoes = opcoes

    def tela(self):
        print(self.titulo)
        for i, opcao in enumerate(self.opcoes):
            print(f"{i + 1}. {opcao}")

    def get_decisao(self):
        decisao = int(input("Escolha uma opção: \n"))
        return decisao

    def run(self):
        while True:
            self.tela()
            decisao = self.get_decisao()
            if decisao == 1:
                break
            elif decisao == 6:
                break
            else:
                print("Opção inválida")

if __name__ == "__main__":
    menu = Menu("Bem vindo à nossa rede de fast food!", ["Definir tamanho da fila com prioridades", "Adicionar novo grupo na fila com prioridades", "Mostrar próximo grupo aguardando", "Preparar próxima refeição", "Entregar refeição", "Gerar simulação"])
    menu.run()