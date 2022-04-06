#Setter = Configurando um valor (=)
#Getter = obter um valor (.)

class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        print("SETTER FOI EXECULTADO")
        nome += " SEI LA"
        self._nome = nome

    @property
    def sobrenome(self):
        return "Desconhecido"




p1 = Pessoa("Tassio")
print(p1.nome)
print(p1.sobrenome)

