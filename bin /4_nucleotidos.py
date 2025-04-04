#Este codigo al recibir una sequencia extrae los primeros 3 nucleotidos

secuencias = input("Ingresa una secuencias separadas por comas:").split(",")
nucleotidos = [secuencia[:3] for secuencia in secuencias]
print(f"Los primeros 3 nucleotidos son: {nucleotidos}")