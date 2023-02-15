# Xor RLLY????

Poeng: 15

## Læremål

 * Forstå hva known plaintext attack er og hvordan det fungerer.
 * Klare å utføre et known plaintext attack mot en kjent dårlig metode for kryptering

## Oppgavetekst

Bjarne har kryptert flagget med xor. Klarer du å dekryptere det?

```
50 82 91 ff 4e 83 86 c1 78 a5 ac e5 6e fa aa e5 72 f9 9f d6 6c b3 a3
```

## Løsning

Vi vet at XOR er brukt. XOR er sårbart for "known plaintext" angrep. Vi vet også at flagget må starte med `PHOENIX{`. 

Dersom vi vet deler av klarteksten, kan vi få ut deler av nøkkelen, fordi `klartekst ^ ciphertekst = nøkkel`.

Dersom vi legger inn `PHOENIX` som input i CyberChef, og bruker `50 82 91 ff 4e 83 86` som Key for XOR-operasjonen, får vi ut nøkkelen. Legg til en "To HEX"-operasjon for å få nøkkelen som HEX:

```
00 ca de ba 00 ca de
```

Siden `00 ca de` repeterer, kan vi gjette at nøkkelen er 4 bytes lang, og er `00 ca de ba`. Nøkkelen kan brukes for å dekryptere flagget, `PHOENIX{xor_n0t_r3Ally}`