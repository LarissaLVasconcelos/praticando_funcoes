##EXERCÍCIO MULTIPLICAÇÃO COM FUNÇÕES

def multiplica(a, b, c, d):
    print(a*b*c*d)

multiplica(2, 3, 4, 6)


##EXERCÍCIO PARA SABER SE O NÚMERO É IMPAR OU PAR:

def numerofuncao(a):
    multiplo = a % 2 == 0

    if multiplo:
        return (f'{a}, é PAR')
    return(f'{a}, é ÍMPAR')

print(numerofuncao(20))
print(numerofuncao(15))
print(numerofuncao(39))

