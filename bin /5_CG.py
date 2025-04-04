secuencia = input("Ingresa una secuencia de ADN:").upper()
g = secuencia.count("G")
c = secuencia.count("C")
porcentaje= (g+c) / len(secuencia) * 100
print(porcentaje)