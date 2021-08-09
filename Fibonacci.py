#Na sequencia de fibonacci, os dois primeiros números são 0 e 1, e todos os seguintes são a soma dos 2 numeros anteriores.
#Escreva um algorítimo que leia um inteiro N (N < 46) e mostre os primeiros N números dessa sequencia.

print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n= 46
while n > 45:
     n = int(input('Um número inteiro menor que 46:'))
cont = 1
anterior = 0
proxima = 1
soma = 1

while cont <= n:

     print(anterior, end=' ')
     cont += 1
     soma = proxima + anterior
     anterior = proxima
     proxima = soma

