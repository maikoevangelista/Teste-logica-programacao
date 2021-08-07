print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
num = int(input('Digite um número de termo para sequência Fibonacci:'))
cont = 1
anterior = 0
proxima = 1
soma = 1

while cont <= num < 46:

     print(anterior, end=' ⇾ ')
     cont += 1
     soma = proxima + anterior
     anterior = proxima
     proxima = soma
print('Fim')
