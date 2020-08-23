# Obs.: Rodar com Python 3.
#
# Suponha que temos um inteiro de 32-bits representando uma cor no formato RGBA:
rgba = 0x3CAEF0FF

# Como poderíamos extrair cada canal de cor em uma variável separada?
# A resposta: bit masking.
#
# Sabemos da existência do operador E (AND) binário, que funciona da seguinte
# forma:
#   01001011
# & 11010110
#   --------
#   01000010
#
# Ou seja, ele serve como um "filtro", gerando 1 quando os dois bits são 1, e
# 0 caso contrário.
print("Exemplo AND: {}".format(bin(0b01001011 & 0b11010110)))

# Certamente, nossa cor em hexadecimal também pode ser convertida para base 2:
# 3    C    A    E    F    0    F    F
# 0011 1100 1010 1110 1111 0000 1111 1111
# Agora, se quisermos o canal R, por exemplo:
#   0011 1100 1010 1110 1111 0000 1111 1111
# & 1111 1111 0000 0000 0000 0000 0000 0000
#   ---------------------------------------
#   0011 1100 0000 0000 0000 0000 0000 0000
red = rgba & 0b11111111000000000000000000000000
print("Vermelho com máscara (bin): {}".format(bin(red)))
print("Vermelho com máscara (hex): {}".format(hex(red)))

# O que é quase o que gostaríamos, pois há vários bits 0 à direita que
# interferem no resultado. Para isso, temos que deslocar os bits para a direita:
# 0011 1100 0000 0000 0000 0000 0000 0000 >> 24
# Deslocamos 24 bits, pois é a quantidade de bits nos canais à
# direita (8 * 3 = 24).
red_shift = red >> 24
print("Vermelho com máscara e deslocamento (bin): {}".format(bin(red_shift)))
print("Vermelho com máscara e deslocamento (hex): {}".format(hex(red_shift)))

# Claro, é incoveniente utilizar binário para tal coisa. Entretanto, é fácil de
# verificar que 0b1111 é o mesmo que 0xF. Assim, podemos extrair o canal verde:
#   3CAEF0FF
# & 00FF0000
#   --------
#   00AE0000
#
# E claro, descolar para direita de 16.
# Obs.: No exemplo abaixo, 0xFF0000 é o mesmo que 0x00FF0000 (podemos ignorar
# zeros à esquerda):
print("Verde com máscara e deslocamento (hex): {}".format(hex((rgba & 0xFF0000) >> 16)))

# Exercício: Utilizando o bit masking, extraia os canais azul e alfa.

