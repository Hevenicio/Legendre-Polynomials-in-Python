import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import numpy as np

#Leitura dos valores de x
dados = pd.read_csv("dados.csv")
df = pd.DataFrame(dados)

def legendre(x,n):
    '''
    Calcula o valor do polinômio de Legendre de qualquer grau utilizando a fórmula de Bonnet:

    $$(n + 1) P_{n+1}(x) = (2n + 1) x P_n(x) - n P_{n-1}$$

    ---------------------------------------------------------
    Params:
    
    x: (float) Ponto da reta real no qual o polinômio será calculado.
    n: (int) Grau do polinômio.
    '''
    if(n == 0):
        return 1
    elif(n == 1):
        return x
    else:
        return ((2*n - 1)*x*legendre(x, n - 1) - (n - 1)*legendre(x, n - 2))/n

#Arrays auxiliares 
c = [0, 1, 2, 3, 4, 5] #Graus dos polinômios a serem calculados
x = np.zeros((len(df['x']),len(c))) #array com os valores de x
P = np.zeros((len(df['x']),len(c))) #array com os valores de P_n(x)

#Realizando o cálculo e o plot
for n in c:
    for i in np.arange(len(df['x'])):
        P[i, n] = legendre(df['x'][i], n)
        x[i, n] = df['x'][i]
    plt.grid(color = 'green')
    plt.xlabel('$x$', fontsize = 17)
    plt.xticks(fontsize = 15)
    plt.yticks(fontsize = 15)
    plt.ylabel('$P_{n}(x)$', fontsize = 17)
    plt.plot(x[:, n], P[:, n],'-', label = '$P_{}(x)$'.format(n))
    
plt.title('Polinômios de Legendre', fontsize = 25)
plt.legend(fancybox = True, shadow = True, fontsize = 15)
plt.show()