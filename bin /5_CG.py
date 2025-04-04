#Este codigo cuenta el porcentaje de nucleotidos G y C en una secuencia de ADN.

secuencia = input("Ingresa una secuencia de ADN:").upper()
g = secuencia.count("G")
c = secuencia.count("C")
porcentaje= (g+c) / len(secuencia) * 100
print(porcentaje)