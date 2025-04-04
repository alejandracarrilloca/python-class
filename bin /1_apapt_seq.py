#Este programa elimina los primeros 14 adaptadores de la secuencia dada. 

with open("data/4_input_adapters.txt" ,"r") as input, open ("results/4_no_input_adapters.txt", "w") as output:
    for linea in input:
      cleanup = linea.strip()[14:]
      print(cleanup, file = output, end="\n")