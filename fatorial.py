# importando as bibliotecas necessarias 
import math
# Recebendo numeros pelo usuario atraves de um loop para verificar se o numero e positivo
while True: 
    print('=' * 62)
    numero = int(input('Informe um número: '))
    if numero <= 0:
        print('O valor inserido esta incorreto, por favot informe um valor valido!')
    elif numero > 0:
        break

# Calculando o fatorial do numero informado
fatorial = math.factorial(numero)

# Mostrando o resultado para o usuario 
print('-' * 62)
print(f'O fatorial de {numero} é {fatorial}')
print('-' * 62)