secuencias = input("Ingresa una secuencias separadas por comas:").upper().split(",")
print(f"\nSecuencias: {secuencias}")

start= [secuencia for secuencia in secuencias if "ATG"  in secuencia]
print(f"Secuencias que inician con ATG: {start}")