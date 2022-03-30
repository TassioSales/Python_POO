from pessoas import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('Tassio', 32)

p1.printa_dados()

p1.comer("banana")
p1.comer("banana")
p1.parar_de_comer()
p1.parar_de_comer()
p1.comer("maça")
p1.falar()
p1.parar_de_comer()
p1.falar("POO")
p1.parar_de_falar()
p1.comer("abacaxi")
p1.falar("Starworls")
p1.parar_de_falar()

print()


p2.comer('Comida')
p2.parar_de_comer()
p2.falar("Abobrinha")
p2.parar_de_falar()
print(p2.get_ano_nascimento())

print(p1.ano_atual)
