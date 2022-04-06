from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Mariazinha')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
print(maquina.escrever)


escritor.ferramenta = caneta
escritor.ferramenta.escrever()


del escritor

print(escritor)
print(caneta.marca)
maquina.escrever()