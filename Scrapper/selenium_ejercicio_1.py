"""
													Estructura de la página

Nombres:                                     Cierre:                                 	Anterior:                              
//*[@id="markets_top"]/tbody/tr[1]/td[2]/a   //*[@id="markets_top"]/tbody/tr[1]/td[3]	//*[@id="markets_top"]/tbody/tr[1]/td[4]	
//*[@id="markets_top"]/tbody/tr[2]/td[2]/a   //*[@id="markets_top"]/tbody/tr[2]/td[3]	//*[@id="markets_top"]/tbody/tr[2]/td[4]	
//*[@id="markets_top"]/tbody/tr[3]/td[2]/a      
//*[@id="markets_top"]/tbody/tr[4]/td[2]/a
//*[@id="markets_top"]/tbody/tr[5]/td[2]/a   

Máximo:                                 	Mínimo:
//*[@id="markets_top"]/tbody/tr[1]/td[5]	//*[@id="markets_top"]/tbody/tr[1]/td[6]
//*[@id="markets_top"]/tbody/tr[2]/td[5]	//*[@id="markets_top"]/tbody/tr[2]/td[6]


//*[@id="markets_top"]/tbody/tr[5]/td[5]	//*[@id="markets_top"]/tbody/tr[5]/td[6]
"""

from selenium import webdriver

def buscar(lista):
	"""Función que recibe una lista del xpath y devuelve el str correspodiente"""
	busqueda=""
	for ele in lista:
		busqueda+=ele.text
	return str(busqueda)

columnas=['Nombre','Cierre','Anterior','Máximo','Mínimo']
path_phantom="C://Users//Edgar//Documents//CursosProgramacion//Phyton//PhamtomJS//phantomjs-2.1.1-windows//bin//phantomjs.exe"
url="https://mx.investing.com/markets/mexico"
# Llenado de la lista xpath_names
xpath_names=[]
for i in range(2,7):
	renglon=[]
	for j in range(1,6):
		if i==2:
			elemento="//*[@id='markets_top']/tbody/tr[%s]/td[%s]/a"%(j,i)
		else:
			elemento="//*[@id='markets_top']/tbody/tr[%s]/td[%s]"%(j,i)
		renglon.append(elemento)
	xpath_names.append(renglon)
# comprobar con: print(xpath_names)

# Búsqueda con el webdriver
driver = webdriver.PhantomJS(path_phantom)
driver.get(url)
i=0
for lista in xpath_names:
	print(columnas[i])
	for ele in lista:
		print(buscar(driver.find_elements_by_xpath(ele)))
	i+=1
	print()
driver.quit() 