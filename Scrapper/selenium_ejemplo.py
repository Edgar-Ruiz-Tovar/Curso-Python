from selenium import webdriver
path_phantom="C://Users//Edgar//Documents//CursosProgramacion//Phyton//PhamtomJS//phantomjs-2.1.1-windows//bin//phantomjs.exe"
url="https://www.plus500.com/es/Trading/Stocks?id=1408&tags=g_sr%2B42715472_cpi%2BWorldSearchSpanish_cp%2B3332097872_agi%2BStocks.Stocks_agn%2Bbolsa%20mexicana%20de%20valores_ks%2Bkwd-311111623833_tid%2Be_mt%2Bc_de%2Bg_nt%2B_ext%2B1010149_loc%2BUURL&%D7%90&gclid=Cj0KCQjwyJn5BRDrARIsADZ9ykGnl2xRJzhQ0eYi8pG-Hn3GUDbrQ7qDqwONr9A2Sm59zqFYjlBuDz8aAglEEALw_wcB"
xpath_stock="//*[@id='tab_Stocks']/tbody/tr[2]/td[5]/span"
xpath_name="//*[@id='tab_Stocks']/tbody/tr[2]/th/span/a" 
driver = webdriver.PhantomJS(path_phantom)
driver.get(url)
precio = driver.find_elements_by_xpath(xpath_stock)
stock="" 
for c in precio: 
	stock = stock + c.text
nombre=driver.find_elements_by_xpath(xpath_name)
name="" 
for c in nombre: 
	name = name + c.text
print(name,stock,sep="\t")