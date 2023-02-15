# Basic steps

Poeng: 25

## Oppgavetekst

Bjarne liker ikke at du så lett fikk tak i flagget i _Almost no work needed_, så han oppgraderte det litt. Programmet fungerer enda likt:

```
./flagChecker [flagg]
```

Eksempel:

```
 $ ./flagChecker PHOENIX{foo-bar}
bad flag

```

Har bjarne klart å stoppe deg denne gangen?

## Læringsmål

 * Bli komfortabel med RE-verktøy
 * Enkel kodeforståelse av psuedo-C/assembly

## Løsning

Fyr opp et RE-verktøy, f.eks ghidra. Programmet er kompilert med symboler, så `main` burde være lett å finne. Fra her kan du se at et flagg genereres(med xor, beklager!) og brukes for å sammenligne med input fra brukeren. Dersom det genererte flagget stemmer med det brukeren ga, er flagget riktig.

Det er flere måter du kan ekstrahere flagget. Du kan:

 * Med en debugger(eller cheat engine!), pause programmet rett før det avslutter. Flagget vil være i minnet
 * Se i koden at bufferen `flag_encrypted` inneholder det krypterte flagget, og at kryptoen er at bufferen blir xoret med `0xba`. Smell det inn i cyberchef, og få flagget:

```
PHOENIX{4223mBLY_m4N}
```