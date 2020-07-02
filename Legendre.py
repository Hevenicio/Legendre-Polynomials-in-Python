from IPython.display import display, Markdown, Latex
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym
import numpy as np

dados = pd.read_csv("dados.csv")
df = pd.DataFrame(dados)

def legendre(x,n):
    if(n == 0):
        return 1
    elif(n == 1):
        return x
    else:
        return ((2*n - 1)*x*legendre(x, n - 1) - (n - 1)*legendre(x, n - 2))/n


c = [0, 1, 2, 3, 4, 5]
x = np.zeros((len(df['x']),len(c)))
P = np.zeros((len(df['x']),len(c)))
d = [x, P]

for n in c:
    for i in np.arange(len(df['x'])):
    	P[i, n] = legendre(df['x'][i], n)
    	x[i, n] = df['x'][i]
    plt.grid(color = 'green')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.plot(x[:, n], P[:, n], '--', label = '$P_{}(x)$'.format(n))

plt.suptitle('Polinômios de Legendre')
plt.legend(fancybox = True, shadow = True)
plt.show()


    	# df2 = pd.DataFrame(d)
    	# df2 = df2.rename(index={0:'x', 1:'y'}).T

# a, b, c, d, e, f = [], [], [], [], [], []
# for i in df['x']:
# 	for j in range(6):
# 		#print(j)
# 		if(j == 0):
# 			a.append(legendre(i, 0))
# 		elif(j==1):
# 			b.append(legendre(i, 1))
# 		elif(j==2):
# 			c.append(legendre(i, 2))
# 		elif(j==3):
# 			d.append(legendre(i, 3))
# 		elif(j==4):
# 			e.append(legendre(i, 4))
# 		elif(j==5):
# 			f.append(legendre(i, 5))
	
# plt.plot(df['x'], a, 'g--o')
# plt.grid(color = 'green')
# plt.style.use('seaborn')
# plt.xlabel('$x$')
# plt.ylabel('$y$')

# plt.show()

# a = []
# b = []
# c = [0, 1, 2, 3, 4, 5]
# d = [b, c]

# for i in df['x']:
# 	a.append(legendre(i, 3))
# 	b.append(i)
# 	df2 = pd.DataFrame(d)
# 	df2 = df2.rename(index={0:'x', 1:'y'}).T