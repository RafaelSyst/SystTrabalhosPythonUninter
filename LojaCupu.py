print('Bem-vindo a loja de gelados do Rafael Dias')
print('            ---Cardápio---')
print('TAMANHO  |   Cupuaçu (CP)     |   Açaí (AC)')
print('   P     |       R$9.00       |    11.00')
print('   M     |       R$14.00      |    16.00')
print('   G     |       R$18.00      |    20.00')

# Armazenar o valor do pedido
valor = 0
valor_soma = 0

# Variaveis de preço
tamanhoPC = 9.0
tamanhoMC = 14.0
tamanhoGC = 18.0

tamanhoPA = 11.0
tamanhoMA = 16.0
tamanhoGA = 20.0

# Repetição caso haja resposta incorreta
while True:
    sabor = input('Escolha o sabor (CP/AC): ')
    if (sabor != 'CP' and sabor != 'AC' and sabor != 'cp' and sabor != 'ac'):
        print('Sabor inválido. Tente novamente.')
        continue
    tamanho = input('Escolha o Tamanho: ')
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G' and tamanho != 'p' and tamanho != 'm' and tamanho != 'g':
        print('Tamanho inválido. Tente novamente.')   
        continue

# Valores dos pedidos      
    if(sabor == 'CP' and tamanho == 'P' or sabor == 'cp' and tamanho == 'p'):
        valor = tamanhoPC
    elif(sabor == 'CP' and tamanho == 'M' or sabor == 'cp' and tamanho == 'm'):
        valor = tamanhoMC
    elif(sabor == 'CP' and tamanho == 'G' or sabor == 'cp' and tamanho == 'g'):
        valor = tamanhoGC    
    elif(sabor == 'AC' and tamanho == 'P' or sabor == 'ac' and tamanho == 'p'):
        valor = tamanhoPA
    elif(sabor == 'AC' and tamanho == 'M' or sabor == 'ac' and tamanho == 'm'):
        valor = tamanhoMA
    elif(sabor == 'AC' and tamanho == 'G' or sabor == 'ac' and tamanho == 'g'):
        valor = tamanhoGA

# Mostrar o valor total na tela
    valor_soma += valor  
    print('Valor total a pagar: R$',valor_soma)
    
# Input para pedir novamente
    resposta = input('Deseja pedir mais alguma coisa? (S/N) ')
    if (resposta == 'S' or resposta == 's'):
        continue
    elif (resposta == 'N' or resposta == 'n'):
        print('Tenha um bom apetite!')
        break
# Caso a resposta no final esteja incorreta    
    else:
        print('Resposta inválida. Inicie novamente.')
        break
    