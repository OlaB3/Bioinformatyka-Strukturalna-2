def Fasta(path):
    sequences = []  
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line.startswith('>'):
                sequences.append(line)  

    return sequences

def Seq():
    seq1 = input("Wprowadz 1. sekwencje: ")
    seq2 = input("Wprowadz 2. sekwencje: ")
    return seq1, seq2

def Choice():

    print("Wybierz opcje: ")
    print("1. Wczytaj pliki fasta")
    print("2. Wpisz recznie")

    ch = input("1/2: ")
    return int(ch)  

if __name__ == "__main__":
    seq1 = ""
    seq2 = ""
    ch = Choice() 
    if ch == 1:
        path1 = input("Podaj sciezke pliku fasta: ")
        path2 = input("Podaj sciezke pliku fasta: ")

        seq1 = Fasta(path1)
        seq2 = Fasta(path2)
        seq1 = str(seq1[0])
        seq2 = str(seq2[0])

        if seq1 and seq2: 
            print("Sekwencje zostaly wczytane z plikow FASTA.")
            print("1. ", seq1)
            print("2. ", seq2)
        else:
            print("Nie udalo sie wczytac")

    elif ch == 2:
        seq1, seq2 = Seq()  

        print("1. ", seq1)
        print("2. ", seq2)