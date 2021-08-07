print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
num= 46
while num > 45:
     num = int(input('Um número inteiro menor que 46:'))
cont = 1
anterior = 0
proxima = 1
soma = 1

while cont <= num:

     print(anterior, end=' ')
     cont += 1
     soma = proxima + anterior
     anterior = proxima
     proxima = soma
