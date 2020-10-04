import sys
import pygame
import random
import matplotlib.pyplot as plt
from math import sqrt,pi

pygame.init()
# pantalla
ANCHO,ALTO=650,650
superficie=pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('Media del diámetro de un Círculo')
# colores
azul,negro=(0,0,255),(0,0,0)
centro=(330,330)
milliseconds = 50

class Punto():

	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

	def __str__(self):
		return f"Punto: ({self.x},{self.y})"

	def recta(self,p):
		pygame.draw.line(superficie, azul, (self.x,self.y), (p.x,p.y), 1)

	def distancia(self,p):
		return int(sqrt((self.x-p.x)**2+(self.y-p.y)**2))

def aleatorio():
	x=random.randint(centro[0]-200, centro[1]+200) # valores de x: (330-200,330+200)
	aa=random.choice([1,-1]) # para que sea arriba (raíz negativa por pantalla volteada) o abajo (raíz positiva)
	y=int(aa*sqrt(40000-(x-330)**2)+330)
	return Punto(x,y)

def simulacion(n):
	medias=[]
	for i in range(n):
		p1=aleatorio()
		p2=aleatorio()
		p1.recta(p2)
		medias.append(p1.distancia(p2))
	#print(f"Aproximación de {n}: {sum(medias)/n}")
	return sum(medias)/n

def grafica(lista):
	plt.scatter(list(range(1,len(lista)+1)),lista,color='blue',linewidth=3,label='Aproximaciones')
	plt.plot([1,len(lista)+1],[4*200/pi,4*200/pi],color='red',linewidth=3,label='Valor real')
	plt.title("Gráfica de medias")
	plt.legend()
	plt.xlabel('n')
	plt.ylabel('media')
	plt.grid(True)
	plt.show()

num=10
medias=[]
while num<=1000:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	superficie.fill(negro) 
	pygame.time.wait(milliseconds) # delay
	# imprimir el texto
	text="n="+str(num)
	fuente = pygame.font.Font(None, 50)
	mensaje = fuente.render(text, 1, (255, 255, 255))
	superficie.blit(mensaje, (15, 10))
	# gráficas
	pygame.draw.circle(superficie,azul,centro,200)
	pygame.draw.circle(superficie,negro,centro,199)
	medias.append(simulacion(num))
	# incremento
	num+=10
	pygame.display.update()

grafica(medias)