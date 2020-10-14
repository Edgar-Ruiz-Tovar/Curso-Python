import matplotlib.pyplot as plt

def graficar_puntos(lista):
	plt.scatter(list(range(1,len(lista)+1)),lista,color='blue',linewidth=3,label='nombre')
	plt.legend()
	plt.grid()
	plt.show()

def graficar_linea(lista):
	plt.plot(list(range(1,len(lista)+1)),lista,color='blue',linewidth=3,label='nombre')
	plt.legend()
	plt.grid()
	plt.show()

graficar_puntos([4,3,2,1])