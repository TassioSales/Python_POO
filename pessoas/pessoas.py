from datetime import datetime

class Pessoa:

    ano_atual = int( datetime.strftime(datetime.now(),"%Y"))

    
    def __init__(self, nome, idade, comendo = False, falando= False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def printa_dados(self):
        print(f'O {self.nome} tem {self.idade}')


    def falar(self, assunto = "Bobeira"):
        if self.comendo:
            print(f'{self.nome} não pode falar')
            return

        if self.falando:
            print(f'{self.nome} já esta falando')
            return

        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando sobre {assunto}')

        print(f'{self.nome} parou de falar')

    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} Ja esta comendo ")
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')


        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo')
            return
        
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

   



    

    #def esta_comendo(self):
        #if self.comendo == True:
           # print(f"O {self.nome} esta comendo")
        #else:
            #print(f"O {self.nome} não esta falando")

    #def esta_falando(self):
        #if self.falando == True:
                #print(f"O {self.nome} esta Falando")
        #else:
            #print(f"O {self.nome} não esta falando ")
