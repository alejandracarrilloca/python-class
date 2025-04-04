#Este codigo convierte una secuencia de ADN a ARN.

secuencias = input("Ingresa una secuencias separadas por comas:").split(",")
arn = [secuencia.replace ("T","U") for secuencia in secuencias]

print(f"\nSecuencia convertida a ARN: {arn}")