R=100 #pago periodico
i=.4 
n=4 #periodos
numerador=1-(1+i)**(-n)
VR=R*numerador/i
VP= R*((1-(1+i)**(-n))/i)
print("VP={}".format(VP))
R=input("Pon el pago periódico: ")