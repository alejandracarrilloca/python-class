#Este codigo cuenta la cantidad de nucleotidos en una secuencia de ADN.

secuencias = input("Ingresa una secuencias separadas por comas:").upper().split(",")

a = [secuencia.count("A") for secuencia in secuencias]
b = [secuencia.count("T") for secuencia in secuencias]
c = [secuencia.count("C") for secuencia in secuencias]
d = [secuencia.count("G") for secuencia in secuencias]

contar_nucleotidos = [a,b,c,d]
print(f"\nCantidad: {contar_nucleotidos}")