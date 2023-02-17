# Familietre

Poeng: 15

## Oppgavetekst

Vi har en server kjørende som gir deg flagget om du gir riktig passord. Du sender passord til den ved å sende HTTP requests med headeren `X-Bjarne-Password`, f.eks slik:

```
curl -H "X-Bjarne-Password: foo.bar.baz" https://familietre.phoenixlan.no
```

Vi har lagt ved passord-generatoren. Vi benytter oss av `Bjarne1988`. Hva er passordet?

## Læringsmål

 * Forstå inheritance

## Løsning


Flagg:

```
PHOENIX{pyTHoN_1nh3r1T4nc3_15_345Y?}
```