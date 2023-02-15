# Almost no work needed

Poeng: 15

## Oppgavetekst

こんにちは！ Bjarne skrev et linux-program som kan sjekke om et flagg stemmer. Du kan bruke det slik:

```
./nowork [flagg]
```

Eksempel:

```
 $ ./nowork PHOENIX{foo-bar}
bad flag
```

Finn flagget!

## Læringsmål

 * Se at tekst ofte lagres direkte i binære filer, og at du kan lete etter det
 * Se at tekst noen ganger lagres over flere bytes for å støtte mer enn 255 tegn

## Løsning

Den Japanske teksten er et hint til at du må tenke utenfor ASCII.

Det er to metoder å løse oppgaven på.

### Lete i fila

Du vil ikke kunne søke i fila etter flagget, siden flagget er i en wide string. Du vil likevel kunne finne flagget om du leker. Det vil ligge på samme sted som annen tekst i programmet. For eksempel, med xxd får jeg:

```
00002000: 0100 0200 0000 0000 5000 0000 4800 0000  ........P...H...
00002010: 4f00 0000 4500 0000 4e00 0000 4900 0000  O...E...N...I...
00002020: 5800 0000 7b00 0000 4e00 0000 3000 0000  X...{...N...0...
00002030: 5f00 0000 4e00 0000 3300 0000 3300 0000  _...N...3...3...
00002040: 6400 0000 5f00 0000 3400 0000 5f00 0000  d..._...4..._...
00002050: 7200 0000 3300 0000 7d00 0000 0000 0000  r...3...}.......
00002060: 506c 6561 7365 2070 726f 7669 6465 2061  Please provide a
00002070: 2066 6c61 670a 4578 616d 706c 653a 202e   flag.Example: .
00002080: 2f66 6c61 6743 6865 636b 6572 205b 666c  /flagChecker [fl
00002090: 6167 5d00 4e69 6365 2074 7279 203a 2900  ag].Nice try :).
000020a0: 2500 0000 6800 0000 7300 0000 0000 0000  %...h...s.......
000020b0: 436f 7272 6563 7420 666c 6167 2100 6261  Correct flag!.ba
000020c0: 6420 666c 6167 0000 011b 033b 2400 0000  d flag.....;$...
000020d0: 0300 0000 58ef ffff 5800 0000 b8ef ffff  ....X...X.......
```


### RE

Fyr opp et RE-verktøy, f.eks ghidra. Programmet er kompilert med symboler, så `main` burde være lett å finne. Fra her vil du finne en referanse til minnet der flagget ligger


## Flagg
```
PHOENIX{N0_N33d_4_r3}
```