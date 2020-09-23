import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver

def buscar(lista):
	busqueda=""
	for ele in lista:
		busqueda+=ele.text
	return str(busqueda)

def medias_moviles(arreglo,p):
    res=[]
    for i in range(len(arreglo)-p+1):
        res.append((arreglo[i]+arreglo[i+1]+arreglo[i+2])/p)
    return np.array(res)

# paths
path_phantom="C://Users//Edgar//Documents//CursosProgramacion//Phyton//PhamtomJS//phantomjs-2.1.1-windows//bin//phantomjs.exe"
url="https://mx.investing.com/currencies/usd-mxn-historical-data"

# búsqueda en el webdriver
valores=np.array(list(range(23)),dtype='float64')
driver = webdriver.PhantomJS(path_phantom)
driver.get(url)
for i in range(23):
	valores[i]=float(buscar(driver.find_elements_by_xpath("//*[@id='curr_table']/tbody/tr[%s]/td[3]"%(i+1))))
#print(valores)

# Graficación
x=np.arange(0,23)
plt.plot(x,valores,color='red',linewidth=3,label='Precio de Apertura')
x=np.arange(1,len(valores)-1)
plt.plot(x,medias_moviles(valores,3),color='blue',linewidth=2,label='Suavizamiento')
plt.xlabel('Tiempo')
plt.ylabel('Precio del Dólar')
plt.legend()
plt.grid(True)
plt.show()