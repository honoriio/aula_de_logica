# importando as bibliotecas necessarias 
import random

#  Lista com os números para sorteio
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# sorteando um numero da lista
numero_sorteado = random.choice(lista)

# tela de apresentação do programa
print('=' * 62)
print('JOGO DO SORTEIO'.center(62))
print('=' * 62)

# mostrando o numero sorteado
print(f'O número ja foi sorteado! Que comecem os jogos...')

# Loop para o usuario inserir o numero até o mesmo acertar, somente apos acertar o mesmo sera encerrado
while True:
    while True:
        numero_usuario = int(input('Informe um número de 1 a 10: '))
        print('-' * 62)
        if numero_usuario > 10:
            print('Número informado invalido, insira o valor novamente!!')
        else: 
            break
    if numero_usuario < numero_sorteado:
        print('Você chutou um numero a baixo do sorteado!')
    elif numero_usuario > numero_sorteado:
        print('Você chutou um número a cima do número sorteado!')
    elif numero_usuario == numero_sorteado:
        print(f'O número sorteado foi {numero_sorteado}')
        print(f'O número digitado foi {numero_usuario}')
        print('-' * 62)
        print('PARABENS você você acertou!!!!')
        break
print('=' * 62)
print('PROGRAMA FINALIZADO...')
print('=' * 62)