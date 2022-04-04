"""
public, protected, private'

"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados
    
    def inserir_cliente(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]



bd = BaseDeDados()

bd.inserir_cliente(1, "Tassio")
bd.inserir_cliente(2, "Lucian")
bd.inserir_cliente(3, "Jesus")
bd.inserir_cliente(4, "Sales")
bd.__dados = "Outra coisa"

print(bd._BaseDeDados__dados)
print(bd.dados)

print()

bd.lista_clientes()
