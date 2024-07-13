class elementoLista:
    def __init__(self, informacao):
        self.informacao = informacao
        self.proximo = None
    def __repr__(self):
        return str(self.informacao)
class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir(self, cor, numero):
        nodo = elementoLista(f"{cor}{numero}")
        if cor == 'V':
            self.inserirSemPrioridade(nodo)
        elif cor == 'A':
            self.inserirComPrioridade(nodo)
        else:
            print("Informação inválida, lembre-se o V - Verde são para pacientes sem prioridade e o A - Amarelo são para pacientes com prioridade.")

    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        elif self.head.informacao[0] == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            anterior = None
            atual = self.head
            while atual is not None and atual.informacao[0] == 'A':
                anterior = atual
                atual = atual.proximo
            if anterior is None:
                nodo.proximo = self.head
                self.head = nodo
            else:
                nodo.proximo = anterior.proximo
                anterior.proximo = nodo

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo

    def imprimirListaEspera(self):
        if self.head is None:
            print("[-->]Lista de espera esta vazia! Meus parabéns todos os pacientes foram atendidos.")
            return

        nodo = self.head
        while nodo is not None:
            print(nodo, end=" -> ")
            nodo = nodo.proximo
        print("None")

    def atenderPaciente(self):
        if self.head is not None:
            paciente = self.head
            self.head = self.head.proximo
            print(f"[-->]Chamando paciente {paciente.informacao}, siga para a sala do médico no final do corredor por favor.")
        else:
            print ("[-->]A fila de pacientes está vazia.")

def menu():
    lista = ListaEncadeada()
    while True:
        print("\nSeja bem vindo ao nosso sistema de atendimento, por favor verifiquei a lista abaixo e insira o que deseja:")
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair do sistema")

        opcaoEscolhida = int(input("[-->]Escolha uma opção entre 1 e 4: "))

        if opcaoEscolhida == 1:
            print("A opção escolhida foi 1 – Adicionar paciente à fila")
            prioridade = str(input("[-->]Informe a prioridade do paciente A - Amarelo(Com prioridade), V - Verde (Sem prioridade): ")).upper()
            if prioridade == "A":
                informacao = int(input("[-->]Informe o número do paciente na fila de espera. Quanto menor for o número maior será a prioridade (Pacientes com prioridade começam em 201): "))
                if informacao >= 201:
                    lista.inserir("A", informacao)
                else:
                    print("[-->]Este número é inválido por já existir ou número inserido é menor do que é aceito.")
            elif prioridade == "V":
                informacao = int(input("[-->]Informe o número do paciente na fila de espera. Quanto menor for o número maior será a prioridade (Pacientes com prioridade começam em 1): "))
                if informacao >= 1:
                    lista.inserir("V", informacao)
                else:
                    print("[-->]Este número é inválido por já existir ou número inserido é menor do que é aceito.")
            else:
                print("[-->]Você informou uma prioridade inválida, por favor verifique.")

        elif opcaoEscolhida == 2:
            print("[-->]A opção escolhida foi 2 – Mostrar pacientes na fila")
            lista.imprimirListaEspera()

        elif opcaoEscolhida == 3:
            print ("[-->]A opção escolhida foi 3 – Chamar paciente")
            lista.atenderPaciente()

        elif opcaoEscolhida == 4:
            print ("[-->]A opção escolhida foi 4 – Sair do sistema")
            print("Encerrando o sistema...Obrigado pelo uso!")
            break

        else:
            print("[-->]A opção escolhida não é válida, por favor tente novamente.")

# Execução do programa
menu()
