from model import model

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()

# ========================================================================= G E T  /  S E T  ================================================================================



    def getOpcao(self):
        return self.opcao


    def setOpcao(self, opcao):
        self.opcao = opcao




#========================================================================= M E N U  ================================================================================



    def menu(self):
        print("Escolha uma das opções abaixo: \n" +
              "\n0. Sair"                           +
              "\n1. Cadastrar"                      +
              "\n2. Consultar"                      +
              "\n3. Atualizar"                      +
              "\n4. Excluir")
        self.setOpcao(int(input()))



# ========================================================================= O P Ç Õ E S ================================================================================



    def operacoes(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.cadastrar()
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            else:
                print("Opção escolhida invalida! Tente novamente!")



# ========================================================================= M E T O D O S ================================================================================


    def cadastrar(self):
        print("Informe o seu nome: ")
        nome = input()
        print("Informe o seu telefone: ")
        telefone = input()
        print("Informe o seu endereço: ")
        endereco = input()
        print("Informe a data de nascimento: ")
        dataDeNascimento = input()
        print(self.modelo.inserir(nome, telefone, endereco, self.transformarData(dataDeNascimento)))



    def transformarData(self, texto):
        separado = texto.split('/')
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]

        return "{}-{}-{}".format(ano,mes,dia)