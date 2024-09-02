print('Bem-vindo a Copiadora do Rafael Dias')

# Valores dos Serviços
dig = 1.10
ico = 1.0
ipb = 0.40
fot = 0.20

valor = 0

# Função para a escolha do serviço
def escolha_servico():
    print('Escolha o serviço desejado')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')

    global servico_escolhido
    global preco

    print('------Escolha o serviço:------ ')
    servico_escolhido = input()

# Relacionar a escolha do input com o preço
    if(servico_escolhido != 'dig' and servico_escolhido != 'ico' and servico_escolhido != 'ipb' and servico_escolhido != 'fot' ):
        print('Escolha inválida. Tente Novamente.')
        escolha_servico()    

    if(servico_escolhido == 'dig'):
        preco = dig
    
    elif(servico_escolhido == 'ico'):
        preco = ico

    elif(servico_escolhido == 'ipb'):
        preco = ipb
    
    elif(servico_escolhido == 'fot'):
        preco = fot
      
    
# Função para número de páginas
def num_pagina():
    global paginas
    global desconto
    # Caso a escolha não seja um número 
    try:   
        paginas = float(input('Entre com a quantidade de páginas: '))
    except ValueError:
        print('Digite apenas números')
        num_pagina()    
    
    # Calculo para os descontos e limite de páginas
    if(paginas >= 20 and paginas < 200):
        desconto = (preco*paginas)*0.85
    
    elif(paginas >= 200 and paginas < 2000):
        desconto = (preco*paginas)*0.80
    
    elif(paginas >= 2000 and paginas < 20000):
        desconto = (preco*paginas)*0.75
    
    elif(paginas > 20000):
        print('Apenas trabalhamos com valores abaixo de 20000 páginas')
        num_pagina()
   
    else:
        print('A partir de 20 páginas você receberá descontos!') 

    
# Função para serviços extras   
def servico_extra():
    global extra
    global valor_extra
    print('Deseja mais algum serviço?')
    print('(1) - Encadernação simples - R$15')
    print('(2) - Encadernação de capa dura - R$40')
    print('(0) - Não desejo mais nada')
    extra = input()

    if(extra == '0'):
        print('Obrigado por trabalhar conosco!')
    
    elif(extra == '1'):
        valor_extra = 15

    elif(extra == '2'):
        valor_extra = 40

    else:
        print('Opção inválida. Tente novamente.')
        servico_extra()

# Execução das funções
escolha_servico()
num_pagina()
servico_extra()
valor_extra_real = valor_extra

if(paginas >= 20):
    print('O valor a ser pago será de: R$',desconto + valor_extra)

else:
    valor = (preco*paginas) + valor_extra_real
    print('O valor a ser pago será de: R$',valor)