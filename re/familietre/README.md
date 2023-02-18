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

Letteste løsning er å importere klassen `Bjarne1988` og kalle get_password. Passordet er `5w4G4d3Ll1c.l3375P33k.c00l5sh.l3375P33k.8jaRn3.IrhAh`

Flagg:

```
PHOENIX{pyTHoN_1nh3r1T4nc3_15_345Y?}
```