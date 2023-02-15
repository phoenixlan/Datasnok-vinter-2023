# Kommunikasjon for agenter

Bjarne har en side-gig som hemmelig agent. Han bruker en modifisert tamagochi for å kommunisere med https://agent.phoenixlan.no - et system for å gi CTF-flagg til hemmelige agenter som han. Klarer du å hente det ut?

Poeng: 25

## Løsning

Dette er en oppgave der vi skal snakke med en http-server og få ut et flagg.

Vi har et par hint:
 * Ordet "agent" blir brukt mange ganger
 * En tamagochi blir brukt for å snakke med serveren

HTTP-headeren `User-Agent` brukes for å fortelle serveren hvilken nettleser du bruker. Det er nødvendig bl.a fordi nettlesere noen ganger oppfører seg forskjellig. Nå for tiden brukes det for det meste for å spore deg på nettet.

En `User-Agent` kan f.eks se slik ut: `Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1`.

Oppgaven løses ved å sende en HTTP GET forespørsel til serveren med ordet "tamagochi" i user-agent strengen. Du kan for eksempel gjøre slik:

```
 $ curl localhost:5000 -H "User-Agent: tamagochi"
{"flag": "PHOENIX{H77p_h34D3rS_Y34H!}"}   

```