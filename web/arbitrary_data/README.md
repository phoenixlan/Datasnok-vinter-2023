# Arbitrary data

Poeng: 20

## Oppgavetekst

Vi har skjult et flagg et sted vi kan fritt legge inn data. Flagget er tilstede i de fleste forespørsler som skjer _etter at du har lastet_ https://delta.phoenixlan.no/. Finner du det?

## Løsning

Siden delta.phoenixlan.no er en SPA, er alle forespørsler etter at siden er lastet til API-serveren https://api.phoenixlan.no/. Din authentication token, `X-Phoenix-Auth`, blir sendt i mesteparten av forespørslene dit.

Tokenen er en JWT-token. I kroppen av en JWT kan vi legge ved hva vi vil. Her er et eksempel på en JWT-token generert av API-serveren våres:

```json
{
  "roles": [
  ],
  "flag": "PHOENIX{JWTS_ARE_AWESOME}",
  "sub": "b729fd1b-1477-4c23-b15d-2c75f707b774",
  "iat": 1676421468,
  "exp": 1676425068
}
```