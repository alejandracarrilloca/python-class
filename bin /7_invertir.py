#Este codigo invierte una secuencia de ADN.

secuencias = input("Ingresa una secuencias separadas por comas:").split(",")
secuencias_inversas = [secuencia [::-1] for secuencia in secuencias]
print(f"\nSecuencia inversa: {secuencias_inversas}")