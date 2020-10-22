# Exercício Python 037 
# Escreva um programa que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será 
# a base de conversão:
num = int(input('Digite um número inteiro qualquer  '))

print(''' Escolha uma das bases para conversão:
[ 1 ] Binário 
[ 2 ] Octal
[ 3 ] Hexadecimal ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção  == 3:
    print('{} convertido para HEXADECIMAL  é igual a {}'.format(num, hex(num)[2:])) 
else:
    print('Opção inválida. Tente novamente.')

