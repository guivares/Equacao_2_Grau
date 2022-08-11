#Ao iniciar o codigo, serao solicitados os valores das variaveis
#Primeiro devera ser inserido o valor de A que sera salvo na variavel valor_a
#Segundo devera ser inserido o valor de B que sera salvo na variavel valor_b
#Terceiro devera ser inserido o valor de C que sera salvo na variavel valor_c
#Em seguida o codigo faz o calculo do valor de delta (delta = b²-4*a*c)
#Em seguida é verificado se delta é menor, igual ou maior que zero para continuação do programa
#Se Delta for menor que zero, será exibida uma mensagem de "Equacao nao possui raizes reais" junto com o grafico em branco, encerrando o programa
#Se Delta for Maior ou igual a zero, o codigo seguira com os calculos restantes.
#Em seguida são realizados os calculos dos valores de X1 e X2 utilizando a formula de bhaskara
#Em seguida é definido os valores do eixo X e eixo Y para o grafico
#Em seguida o grafico é exibido para o usuario.

#Import de bibliotecas
import matplotlib.pyplot as plt
import numpy as np

#Imputar valor de A
valor_a = float(input("Digite o valor de A: "))
#Imputar valor de B
valor_b = float(input("Digite o valor de B: "))
#Imputar valor de C
valor_c = float(input("Digite o valor de C: "))
#Calculo de Delta
delta = ((valor_b)**2)-(4*valor_a*valor_c)

#Funcoes para calculos de X1 e X2
if delta < 0:
    print("A equação não possui raizes reais.")

valor_x1 = (-(valor_b)+((delta)**(1/2)))/(2*valor_a)
valor_x2 = (-(valor_b)-((delta)**(1/2)))/(2*valor_a)
valor_xV = -(valor_b)/(2*valor_a)
valor_yV = -(delta)/(4*valor_a)

print("Delta=", delta)
print("X1=", valor_x1)
print("X2=", valor_x2)
print("Xv=", valor_xV)
print("Yv=", valor_yV)

#listas que serão utilizadas
eixo_x = []
eixo_y = []
zero = []

#valor de variacao
variacao = abs(valor_x1 - valor_x2)
if variacao < 3:
    variacao = 3
print(variacao)

#funcao para definicao do eixo x e eixo y
for x in np.arange(valor_x1 - variacao, valor_x2 + variacao, variacao / 100):
    y= valor_a * (x ** 2 ) + valor_b * (x) + valor_c
    eixo_x.append(x)
    eixo_y.append(y)
    zero.append(0.0)

#exibicao do grafico
plt.plot(eixo_x,eixo_y,color="blue")
plt.plot(eixo_x,zero,color="black")
plt.plot(eixo_x, eixo_y, label='Eq. 2° Grau')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Equação do Segundo Grau')
plt.show()