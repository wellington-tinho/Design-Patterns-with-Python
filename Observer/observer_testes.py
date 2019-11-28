class Eu:
    def __init__(self):
        self.__acao = 'Dormindo' 
        self.observer =[]
    
    @property
    def acao(self):
        return  self.__acao
    
    @acao.setter
    def acao(self,valor):
        self.__acao=valor
        self.update_obervers()
    
    def update_obervers(self):
        for i in self.observer:
            i.__call__()
    
    def linkagem(self,amigo):
        self.observer.append(amigo)

class Amigo():
    def __init__(self,pessoa_eu):
        pessoa_eu.linkagem(self) #enviando o proprio objeto
        self.wrtinho=pessoa_eu

    def __call__(self):
        print(f'Ja que vc esta {self.wrtinho.acao}, bora tomar um café ')

print("Antes da linkagem")
eu = Eu()

eu.acao='estudando'
print(eu.acao)
print("\n Depois da linkagem")
eu = Eu()
amigo = Amigo(eu)
eu.acao='estudando'
eu.acao ='Fazendo qualquer coisa'
print(eu.acao)
