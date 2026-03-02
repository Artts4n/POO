class Aluno:
    def __init__(self, nome, matricula):
        # Atributos privados:
        self.__nome = None 
        self.__matricula = None
        self.__notas = []

        self.set_nome(nome)
        self.set_matricula(matricula)

    # Getter para o nome:
    def get_nome(self):
        return self.__nome
    
    # Setter para o nome, com validação: não pode ser vazio ou conter apenas espaços
    def set_nome(self, nome):
        if nome: # Verifica se o nome não é vazio ou apenas espaços
            self.__nome = nome
        else:
            print("Nome inválido. Por favor, insira um nome válido.")

    # Getter para a matrícula
    def get_matricula(self):
        return self.__matricula

    # Setter para matrícula com validação: número entre 8 e 10 dígitos
    def set_matricula(self, matricula):
        if matricula.isdigit() and 8 <= len(matricula) <= 10:
            self.__matricula = matricula
        else:
            print("Matrícula inválida. Deve conter entre 8 e 10 dígitos numéricos.")

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida!")

    def calcular_media(self): # Retorna a média das notas do aluno ou 0 se não houver notas.
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)
    
    def mostrar_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"matricula: {self.get_matricula()}")
        print(f"média: {self.calcular_media()}")
    
aluno1 = Aluno("João", "2025101035")
aluno1.adicionar_nota(8.0)
aluno1.adicionar_nota(7.0)

aluno2 = Aluno("Gabriel","1234567899")
aluno2.adicionar_nota(9.8)
aluno2.adicionar_nota(6.8)

aluno3 = Aluno("Gustavo","1234567889")
aluno3.adicionar_nota(9.1)
aluno3.adicionar_nota(4.1)

aluno1.mostrar_dados()

aluno2.mostrar_dados()

aluno3.mostrar_dados()
