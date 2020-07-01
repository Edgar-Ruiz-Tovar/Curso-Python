# Python nos sirve para simplificar muchas tareas
"""
	Por ejemplo imagina que queramos calcular la velocidad de un objeto. Entonces en vez de buscar
	o en vez de tener que aprenderte ésta fórmula y hacer los cálculos tú vamos a hacer un pequeño
	programa en el cual tú des los parámetros que conoces y te calcule la Velocidad.
"""
distancia=4 # creamos la varible distancia donde nosotros le podemos decir cuánto queremos que valga
tiempo=6
velocidad=distancia/tiempo # y la velocidad será la división
print("La velocidad es: V={}/{}={}".format(distancia,tiempo,velocidad))
"""
	Entonces lo que hicimos fue primero decirle al programa cuánto valían la distancia y cuánto valía el tiempo,
	con esto el programa ya sabe que la velocidad es la división de estos dos y al final imprimimos con un formato
	bonito.
	Nota1: los comentarios de varias líneas están escritos entre 6 comillas.
	Nota2: el .format() nos va a imprimir el formato de la variable. 
"""
# Nota3: los comentarios de una sola línea se escriben con el símbolo del numeral
# Ahora imagina que quieres tener una fórmula que te calcule el interés simple
# Creación de variables:
ci=50 # capital inicial 
i=0.1 # tasa de interés
n=8 # número de periodos
# Sustitución en la fórmula
cf = ci*(1+n*i)
# Imprimir resultado
print("Aplicando la fórmula de interés simple se obtiene que: cf={}(1+{}x{})={}".format(ci,i,n,cf))
"""
	Ejercicios: 
	1. Realiza un programa que me calcule el valor presente de una anualidad vencida.
	2. Realiza un programa que me calcule el valor futuro de una anualidad vencida.
"""

# Variables.
""" 
	Una variable es un espacio de la memoria de nuestra computadora al cual le asignamos un nombre y un tipo.
	Las variables en cualquier tipo de lenguaje son: 
	1. Enteras: números enteros. Se escriben como int
	2. Flotantes: números decimales. Se escriben como float
	3. Strings: cualquier conjunto de caracteres. Se escriben como str
	4. Booleanos: verdadero y falso (0,1). Se escriben True y False
"""
# Enteros
n=5 # variable de tipo int
# Puedo sumarle un número y me dará el resultado de su suma
print(n+4)
# Así como otras operaciones básicas
print(f"Resta: {n-8}")
print(f"Multiplicación: {n*6}")
print(f"División: {n/2}")
print(f"Elevar: {n**3}")
print(f"Módulo: {n%2}")

# Flotantes
n=13.5 # variable de tipo float
# las funcionalidades son iguales a la de los enteros
# convertir un dato de tipo entero a flotante
x=5
print(type(x)) # con type puedes saber el tipo de dato
x=float(x)
print(type(x))

# Strings
cadena1="Hola Mundo" # variable de tipo str
print(cadena1)
# Algo muy usual que haremos será concatenar cadenas
cadena2="Otra cadena"
print(cadena1+cadena2)
print(cadena1+" "+cadena2) # con más presentación
# podemos acceder a los caracteres de la cadena mediante índices
print(cadena1[2]) # accedemos al tercer caracter de la cadena1
print(cadena1[-1]) # accedemos al último caracter de la cadena1
# Uso del slicing
print(cadena1[0:2]) # [inicio:fin]

# Booleanos
valor=True # variable de tipo V/F
# se usan para saber el valor de verdad de ciertas sentencias
print(3<5) # ¿3 es menor a 5?
print(3==5) # ¿3 es igual a 5?
print(valor==True) # ¿la variable valor es True?

# Otros tipos de datos (variables)

# Listas
# Las listas son un tipo compuesto de datos ya que puede almacenar diferentes tipos de datos
lista_vacia=[] # lista vacía (uso de notación serpiente)
lista=[1,2,3,4]
print(lista[0]) # imprime su primer elemento
print(lista[-1]) # ahora el último
lista=["Hola",3,8.9,False] # aquí podemos ver cómo ahora tenemos una lista con diferentes tipos de datos
print(lista)
# Método append()
# Nos sirve para añadir un elemento al final de una lista
lista.append(True)
print(lista)
# Por último veamos que podemos modifcar los valores de las listas
lista_nueva=[1,2,"3","4"]
print(lista_nueva)
lista_nueva[2]=3 # el valor "3" lo modificamos por 3
print(lista_nueva)

# Tuplas
# Son los mismo que las listas sólo que son inmutables. Esto quiere decir que no podremos agregar nuevos 
# elementos a las tuplas ni podremos modificarlos.
tupla=(1,2,3) # se escriben entre paréntesis a diferencia de las listas que se escriben entre []
#tupla.append(2) # nos dará error pues no podemos agregar elementos
#tupla[1]=2 # otro error pues no podemos modificar elementos

# Ciclos for()
# Los ciclos nos sirven para evitar tener que repetir muchas veces una misma instrucción. El ciclo for()
# nos es muy útil ya que tiene dos caracterizaciones.
# ciclo en lista
numeros=[1,2,3,4]
for numero in numeros:
	print(numero)
# como este ciclo for va recorriendo cada elemento de la lista y luego nos lo imprime
