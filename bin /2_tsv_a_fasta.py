#Este codigo convierte un archivo en formato TSV a formato FASTA.

with open("dna_sequences.txt", "r") as input, open ("dna_sequence.fa", "w") as output:
    contenido = input.read().strip().splitlines()
    print(f"\n{contenido}")

    for linea in contenido:
      id, seq = linea.strip().split()
      print(f">{id}\n{seq.upper()}\n", file = output, end="\n")