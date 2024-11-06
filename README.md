Kod implementuje algorytm dopasowywania sekwencji DNA, który oblicza najlepsze dopasowanie lokalne między dwoma sekwencjami, umożliwiając zarówno wczytywanie danych z plików FASTA, jak i ręczne wprowadzanie sekwencji przez użytkownika.

Fasta() – funkcja wczytująca sekwencję DNA z pliku w formacie FASTA i zwracająca je jako listę. 
Seq() – funkcja umożliwiająca wprowadzanie dwóch sekwencji DNA na wejście ręcznie przez użytkownika. 
Choice() – funkcja, która ułatwia decyzję użytkownika, czy chce wprowadzić sekwencje z pliku, czy też ręcznie. 
Table() – funkcja wyświetlająca oraz zapisująca w pliku tabelę wyników porównania sekwencji, uwzględniając ich dopasowanie.
Match() – funkcja służąca do aktualizowania wartości w tabeli dopasowanie w przypadku napotkania znaku równości w sekwencjach. 
Mis() – funkcja służąca do aktualizowania wartości w tabeli dopasowanie w przypadku napotkania znaku różnicy w sekwencjach. 
Score() – funkcja śledząca najkrótszą ścieżkę, dopasowująca i tworząca wynikowe sekwencje oraz zapisująca je do pliku. 
Algorithm() – funkcja implementująca algorytm dopasowywania lokalnego, oblicza wartości dopasowania, zapisuje tabelę i wynik dopasowania do pliku.
