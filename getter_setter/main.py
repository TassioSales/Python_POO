class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percetual):
        self.preco = self.preco - (self.preco * (percetual / 100))


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.replace('A', '@')

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, value):
        if isinstance(value, str):
            value = float(value.replace("R$", ''))
        self._preco = value



if __name__ == "__main__":
    p1 = Produto('CAMISETA', 50)
    p1.desconto(10)
    print(p1.nome, p1.preco)


    p2 = Produto('CANECA', 'R$45')
    p2.desconto(10)
    print(p2.nome, p2.preco)