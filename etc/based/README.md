# Based

Poeng: 5

## Oppgavetekst

Bjarne har enkodet et flagg: `UEhPRU5JWHtTVXBFcl84NHNlZF80TV9pX3JpOUh0fQ==`. Kan du dekode det?

## Læringsmål

 * Forstå hva base64 er

## Løsning

Vi kan se at det er snakk om base64:

 * Tittelen på oppgaven er "based"
 * At flagget inneholder bokstaver, tall, og likhetstegn, pleier å være dead giveaway på at det er base64-enkoded

En måte oppgaven kan løses på er ved å kaste teksten inn i cyberchef og velge "from base64" fra listen over operasjoner. Da får du flagget:

```
PHOENIX{SUpEr_84sed_4M_i_ri9Ht}
```

Du kan også f.eks løse oppgaven i JavaScript slik:

```js
atob("UEhPRU5JWHtTVXBFcl84NHNlZF80TV9pX3JpOUh0fQ==");
```

Eller i python slik:

```py
import base64
base64.b64decode("UEhPRU5JWHtTVXBFcl84NHNlZF80TV9pX3JpOUh0fQ==")
```