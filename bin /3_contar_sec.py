with open("secuencias.fasta", "r") as input:
    lineas = input.readlines()

    lineas_filtradas = [linea for linea in lineas if linea.startswith(">")]
    print(f"El numero de secuencias es: {len(lineas_filtradas)}")