import pandas as pd
import matplotlib.pyplot as plt

# leemos el archivo csv y lo guardamos en df
df=pd.read_csv('calificaciones.csv')
criterios=['Tareas','Parcial 1','Parcial 2','Parcial 3']
# convertimos a float() las calificaciones de los parciales y las tareas
for criterio in criterios:
	df[criterio]=df.apply(lambda row: float(row[criterio]),axis=1)
# añadimos la columna de la calificación final
df.insert(5,'Final',[0,0,0,0]) # método insert(posicion,nombre,valores)
# sacamos la calificación final
for i in range(4):
	# total_parcial tendrá la suma de las calificaciones de los 3 parciales
	total_parcial=sum(df.loc[i,criterios[1:]]) # df.loc[fila,[columnas]]
	# y la calificación final vendrá determinada por los porcentajes correspondientes 
	df.loc[i,'Final']=0.3*df.loc[i,'Tareas']+0.7*total_parcial/3

def parciales(indice):
	plt.plot(['Parcial 1','Parcial 2','Parcial 3'],df.loc[indice,criterios[1:]],color='green',linewidth=2,
		label='Rendimiento de %s'%(df.loc[indice,'Alumno']))
	plt.title('Calificaciones Parciales')
	plt.xlabel('Parciales')
	plt.ylabel('Calificación')
	plt.legend()
	plt.show()

def calificacion_final():
	colores=["red","green","blue","#DD98AA"]
	plt.pie(df.Final,colors=colores,labels=df.Alumno,autopct="%1.1f%%")
	plt.axis("equal")
	plt.title("Porcentaje respecto a la calificación")
	plt.show()

def calificacion_tareas():
	plt.bar([1,2,3,4],df.Tareas,tick_label=df.Alumno,width=0.5,color='orange')
	# tick_label nos sirve para dar un nombre a las columnas (predeterminado números)
	plt.title('Calificación de las tareas')
	plt.xlabel('Alumno')
	plt.ylabel('Calificación')
	plt.show()

while True:
	opc=int(input(
		"Elige una opción:\n1. Gráfica del rendimiento por parciales.\n2. Porcentaje de las calificaciones.\n3. Gráfica de las tareas.\n4. Imprimir base de datos.\n5. Salir.\n"
		))
	if opc==1:
		for i in range(4):
			parciales(i)
	elif opc==2:
		calificacion_final()
	elif opc==3:
		calificacion_tareas()
	elif opc==4:
		print(df)
	elif opc==5:
		break