class upercase():
    def __init__(self,f):
        self.f=f
        print(f'passou pelo init {self.f}')
    def __call__(self,*args):
        self.f(args[0].upper())
        print('passou pelo call')

@upercase
def nome(nome):
    print('nome: %s'%nome)

nome('palavra em minuscula')
