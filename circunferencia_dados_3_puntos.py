import sys
import pygame
from math import sqrt

pygame.init()
# pantalla
ANCHO,ALTO=1000,600
superficie=pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption('Círculo dados 3 puntos')
# colores
blanco,verde,azul,negro=(255,255,255),(0,255,0),(0,0,255),(0,0,0)

class Punto():
	"""docstring for Punto"""
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

	def __str__(self):
		return f"Punto: ({self.x},{self.y})"

	def punto_medio(self,p):
		medio=Punto((self.x+p.x)//2,(self.y+p.y)//2)
		return medio

	def distancia(self,p):
		return int(sqrt((self.x-p.x)**2+(self.y-p.y)**2))

	def recta(self,p,m=False):
		if m:
			pygame.draw.line(superficie, verde, (self.x,self.y), (p.x,p.y), 2)
		else:
			pygame.draw.line(superficie, blanco, (self.x,self.y), (p.x,p.y), 2)

	def pendiente(self,p):
		return (p.y-self.y)/(p.x-self.x)

	def escribir_ecuacion(self,m):
		if -m*self.x+self.y<0:
			return f"y={m}x{-m*self.x+self.y}"
		else:
			return f"y={m}x+{-m*self.x+self.y}"

	def ecuacion(self,m,x):
		return self.y+m*(x-self.x) # lo sumamos porque la pantalla gráfica está volteada


print("Puntos")
A=Punto(300,140)
print(str(A))
B=Punto(700,170)
print(str(B))
C=Punto(580,420)
print(str(C))
centro=Punto(495,227)

print()

print("Obtenemos los puntos medios")
M1=A.punto_medio(B)
print(str(M1))
M2=B.punto_medio(C)
print(str(M2))
M3=C.punto_medio(A)
print(str(M3))

print()

print("Pendientes de las rectas")
print(f"m1={A.pendiente(B)}")
print(f"m2={B.pendiente(C)}")
print(f"m3={C.pendiente(A)}")

print()

print("Ecuaciones de las rectas que unen a los puntos A,B y C")
print(f"La ecuación de la recta AB es: {A.escribir_ecuacion(A.pendiente(B))}")
print(f"La ecuación de la recta BC es: {B.escribir_ecuacion(B.pendiente(C))}")
print(f"La ecuación de la recta CA es: {C.escribir_ecuacion(C.pendiente(A))}")

print()

print("Ecuaciones de las medianas")
print(f"La ecuación de la mediana de la recta AB es: {M1.escribir_ecuacion(-1/A.pendiente(B))}")
print(f"La ecuación de la mediana de la recta BC es: {M2.escribir_ecuacion(-1/B.pendiente(C))}")
print(f"La ecuación de la mediana de la recta CA es: {M3.escribir_ecuacion(-1/C.pendiente(A))}")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# pinta pantalla
	superficie.fill(negro)
	# ahora el círculo (porque importa el orden en que pintemos las cosas)
	pygame.draw.circle(superficie,azul,(495,227),A.distancia(centro))
	# dibujamos el triángulo e imprimimos la pendiente de cada recta
	A.recta(B)
	B.recta(C)
	C.recta(A)
	# dibujamos las medianas
	Punto(0,M1.ecuacion(-1/A.pendiente(B),0)).recta(Punto(1000,M1.ecuacion(-1/A.pendiente(B),1000)),True)
	Punto(0,M2.ecuacion(-1/B.pendiente(C),0)).recta(Punto(1000,M2.ecuacion(-1/B.pendiente(C),1000)),True)
	Punto(0,M3.ecuacion(-1/C.pendiente(A),0)).recta(Punto(1000,M3.ecuacion(-1/C.pendiente(A),1000)),True)

	pygame.display.update()