n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o Valor 2: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \na multiplicação é {} \ne a divisão é {}'.format(s ,m, d),end=' ')
# \n = Quebra de linha
# ,end='' = Não qubrar linha
print('A divisao inteira é {} e a potencia é {}'.format(di, e))
