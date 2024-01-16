# Importando as bibliotecas
import time
# apresentação do programa 
print('=' * 62)
print('CONTAGEM'.center(62))
print('=' * 62)

# Entrada de valores pelo usuario 
valor = int(input('Insira um valor inteiro maior que 1 : '))

# Loop de contagem
for i in range(1, valor + 1):
    contagem = i + 1
    print(i)
    time.sleep(1)