from classes import Endereco, Cliente

cliente1 =  Cliente("Luiz", 32)
cliente1.insere_endereco("Brasilia", 'DF')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()



cliente2 = Cliente("Marcos", 22)
cliente2.insere_endereco("Goiania", 'GO')
cliente2.insere_endereco("Rio de Janeiro", "RJ")
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()


cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', "SP")
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()



print("#" * 150)


