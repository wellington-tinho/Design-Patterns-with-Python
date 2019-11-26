"""
Uso de Decorators ultilizando args e kargs
"""

def funcao_decorada(funcao_original):
    def funcao_dentro(*args,**kargs):
        print(f"Executando Função {funcao_original.__name__} dentro da função decorada")
        funcao_original(*args,**kargs)
    return funcao_dentro

@funcao_decorada
def Pessoa_teste(nome,idade):
    print(f"Pessoa {nome} criada com idade {idade}")

Pessoa_teste('wellington',21)
