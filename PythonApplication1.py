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

def Table(seq1, seq2, table, file):
    if len(seq1) <= len(seq2):
        len1 = len(seq1)
        len2 = len(seq2)
    else:
        len1 = len(seq2)
        len2 = len(seq1)
        x = seq1
        seq1 = seq2
        seq2 = x

    pink = "\033[95m"   
    reset = "\033[0m"   

    if len(seq1) <= len(seq2):
        len1 = len(seq1)
        len2 = len(seq2)
    else:
        len1 = len(seq2)
        len2 = len(seq1)
        x = seq1
        seq1 = seq2
        seq2 = x

    header = "      " + pink + " ".join(f" {letter}" for letter in seq1) + reset
    print(header)

    zero_row = "    0 " + " ".join(f"{table[0][j]:>2}" for j in range(1, len1 + 1))
    print(zero_row)

    for i in range(1, len2 + 1):
        row = " " + pink + seq2[i - 1] + reset + " " + f"{table[i][0]:>2} " 
        row += " ".join(f"{table[i][j]:>2}" for j in range(1, len1 + 1))  
        print(row)

    for row in table:
        file.write(" ".join(map(str, row)) + "\n")

def Match(table, i, j, match, gap):
    if i + 1 < len(table) and j + 1 < len(table[0]):
        table[i+1][j+1] = max(
            table[i][j] + match,
            table[i+1][j] + gap,
            table[i][j+1] + gap,
            0
        )
    return table

def Mis(table, i, j, mismatch, gap):
    if i + 1 < len(table) and j + 1 < len(table[0]):
        table[i+1][j+1] = max(
            table[i][j] + mismatch,
            table[i+1][j] + gap,
            table[i][j+1] + gap,
            0
        )
    return table

def Score(seq1, seq2, pos, table, match, mismatch, gap, file):
    scr1 = []
    scr2 = []
    i, j = pos

    while table[i][j] != 0:
        if i > 0 and j > 0 and seq1[j - 1] == seq2[i - 1] and table[i][j] == table[i-1][j-1] + match:
            scr1.append(seq1[j - 1])
            scr2.append(seq2[i - 1])
            i, j = i - 1, j - 1
        elif i > 0 and j > 0 and table[i][j] == table[i-1][j-1] + mismatch:
            scr1.append(seq1[j - 1])
            scr2.append(seq2[i - 1])
            i, j = i - 1, j - 1
        elif i > 1 and j > 1 and table[i][j] == table[i][j-1] + gap == table[i-1][j] + gap:
            if table[i - 1][j - 2] >= table[i - 2][j - 1]:
                scr1.append(seq1[j - 1])
                scr2.append('-')
                j -= 1
            else:
                scr1.append('-')
                scr2.append(seq2[i - 1])
                i -= 1
                
        elif i > 0 and (table[i][j] == table[i-1][j] + gap):
            scr1.append('-')
            scr2.append(seq2[i - 1])
            i -= 1
        else:
            scr1.append(seq1[j - 1])
            scr2.append('-')
            j -= 1

    scr1 = ''.join(scr1[::-1])
    scr2 = ''.join(scr2[::-1])
    path = []
    i = 0
    for i in range(len(scr1)):
        if scr1[i] == scr2[i]:
            path.append('*')
        elif scr1[i] == '-' or scr2[i] == '-':
            path.append(' ')
        else:
            path.append('|')
        i -= 1
    path = ''.join(path)
    print()
    print("\033[92m", scr1, "\033[0m")
    print("\033[95m", path, "\033[0m")
    print("\033[92m", scr2, "\033[0m")

    file.write("\n")  
    file.write(f"{scr1}\n") 
    file.write(f"{path}\n")  
    file.write(f"{scr2}\n")


def Algorithm(seq1, seq2, output_file="output.txt"):
    match = int(input("Podaj wartosc match: "))
    mismatch = int(input("Podaj wartosc mismatch: "))
    gap = int(input("Podaj wartosc gap: "))
    maks = 0

    if len(seq1) <= len(seq2):
        len1 = len(seq1)
        len2 = len(seq2)
    else:
        len1 = len(seq2)
        len2 = len(seq1)
        x = seq1
        seq1 = seq2
        seq2 = x

    table = [[0 for _ in range(len1 + 1)] for _ in range(len2 + 1)]

    for i in range(len2):  
        for j in range(len1):  
            if seq2[i] == seq1[j]:
                table = Match(table, i, j, match, gap)
            else:
                table = Mis(table, i, j, mismatch, gap)
            if table[i+1][j+1] > maks:
                maks = table[i+1][j+1]
                pos = (i+1, j+1)


    with open(output_file, "w") as f:
        Table(seq1, seq2, table, f)
        f.write(" ")
        Score(seq1, seq2, pos, table, match, mismatch, gap, f)

if __name__ == "__main__":
    seq1, seq2 = "", ""
    ch = Choice()
    if ch == 1:
        path1 = input("Podaj sciezke pliku fasta: ")
        path2 = input("Podaj sciezke pliku fasta: ")
        seq1, seq2 = Fasta(path1)[0], Fasta(path2)[0]
        if seq1 and seq2:
            print("Sekwencje zostaly wczytane z plikow FASTA.")
            print("1. ", seq1)
            print("2. ", seq2)
        else:
            print("Nie udalo sie wczytac sekwencji.")
    elif ch == 2:
        seq1, seq2 = Seq()
        print("1. ", seq1)
        print("2. ", seq2)

    Algorithm(seq1, seq2, output_file="wyniki.txt")