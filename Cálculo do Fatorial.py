#O fatorial de um número n é representado por n!
# que é obtido a partir da multiplicação de todos os seus antecessores até o número um.
#n! = nx(n - 1)x(n -2)x...x1

print('-'*30)
print('Cálculo do Fatorial')
print('-'*30)
n= 41
while n > 40:
    n= int(input('digite um numero para calcular o seu Fatorial:'))

f = 1
print('calculando fatorial {}! '.format(n), end=' ')
while  n >0:
    f = f * n
    n-= 1
print('{}'.format(f))
