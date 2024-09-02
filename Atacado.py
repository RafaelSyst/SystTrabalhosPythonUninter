print('Bem-vindo a Loja Rafael Dias')
valor = float(input('Insira o valor do produto:'))
quantidade = int(input('Insira a quantidade de produtos:'))

# Armazena o valor total da compra dos produtos
total = valor*quantidade

# Caso o valor seja acima de R$2.500 e menor que R$6.000, há um desconto de 4%
if (total>= 2500 and total<6000):
    print('Valor SEM desconto: R$',total)
    desconto = total*0.96
    print('Valor COM desconto: R$',desconto)

# Caso o valor seja acima de R$6.000 e menor que R$10.000, há um desconto de 7%
elif (total>= 6000 and total<10000):
     print('Valor SEM desconto: R$',total)
     desconto = total*0.93
     print('Valor COM desconto: R$',desconto)

# Caso o valor seja acima de R$10.000, há um desconto de 11%
elif total>=10000:
     print('Valor SEM desconto: R$',total)
     desconto = total*0.89
     print('Valor COM desconto: R$',desconto)

# Caso o valor seja abaixo de R$2500, não haverá desconto
else:
    print('Valor total: R$',total)
    print('Compras a partir de R$2500,00 terão desconto')
    
