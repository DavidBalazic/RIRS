#  Evidenca letenja projekt

## Struktura projekta

    Backend: FastAPI
    Frontend: Svelte
    UI: shadcn-svelte
    Database: MySQL

##   Git Flow

Projekt uporablja Git flow strategijo za efektivno organizacijo branch-ov

Feature Branch (feat/naziv-funkcionalnosti): Namenjen razvoju posameznih funkcionalnosti. Vsaka nova funkcionalnost dobi svojo feature vejo, ki izhaja iz develop veje. Primer imena: feat/moja-funkcionalnost.

Develop Branch (develop): Glavna veja za integracijo novih funkcionalnosti in skupno testiranje. Vse feature veje se združujejo (merge) v develop, ki predstavlja trenutno razvojno različico projekta.

Release Branch (release/vX.X): Uporablja se za pripravo končne verzije pred izidom (release). Na tej veji se izvajajo zadnji popravki, popravki verzij, optimizacije in končna testiranja. Ko je vse pripravljeno, se združi v main.

Main Branch (main): Primarna veja za produkcijo, ki vsebuje vedno zadnjo stabilno verzijo projekta. Vsaka sprememba v tej veji je preverjena, preizkušena in pripravljena za uporabnike.
