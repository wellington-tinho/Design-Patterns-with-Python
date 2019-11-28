class Refrigerante():
    instancia = None
    def __new__(cls,nome):
        if Refrigerante.instancia is None:
            Refrigerante.instancia=object.__new__(cls)
            Refrigerante.instancia.marca = nome
        return Refrigerante.instancia

        
    def get_nome(self):
        return self.marca


fanta = Refrigerante('fanta')
print(fanta.get_nome())


coca = Refrigerante('coca')
#quando vc descobre que a coca é fanta
print(coca.get_nome())