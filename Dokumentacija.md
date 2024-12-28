# Dokumentacija spletne aplikacije: Evidenca letov

**Avtor:** Jeran Benjamin, Alen Šaruga

**Datum:** 10. 11. 2024

---

## Kazalo vsebine

1. [Opis aplikacije](https://www.notion.so/RIRS-Retrospektiva-sprintov-13a9c99797c9809ba39ac930366ea9b5?pvs=21)
2. [Funkcionalnosti](https://www.notion.so/RIRS-Retrospektiva-sprintov-13a9c99797c9809ba39ac930366ea9b5?pvs=21)
    - [Leti](https://www.notion.so/RIRS-Retrospektiva-sprintov-13a9c99797c9809ba39ac930366ea9b5?pvs=21)
    - [Zgodovina letov](https://www.notion.so/RIRS-Retrospektiva-sprintov-13a9c99797c9809ba39ac930366ea9b5?pvs=21)
    - [Letala](https://www.notion.so/RIRS-Retrospektiva-sprintov-13a9c99797c9809ba39ac930366ea9b5?pvs=21)
3. [Tehnične zahteve](https://www.notion.so/RIRS-Retrospektiva-sprintov-13a9c99797c9809ba39ac930366ea9b5?pvs=21)
4. [Navodila za uporabo](https://www.notion.so/RIRS-Retrospektiva-sprintov-13a9c99797c9809ba39ac930366ea9b5?pvs=21)
5. [Namestitev](https://www.notion.so/RIRS-Retrospektiva-sprintov-13a9c99797c9809ba39ac930366ea9b5?pvs=21)
6. [Podpora](https://www.notion.so/RIRS-Retrospektiva-sprintov-13a9c99797c9809ba39ac930366ea9b5?pvs=21)

---

## Opis aplikacije

**Evidenca letov** je spletna aplikacija, ki uporabnikom omogoča spremljanje letov in razpoložljivih letal. Aplikacija je zasnovana za enostavno upravljanje z informacijami o prihajajočih in preteklih letih ter evidenco letal, ki jih uporabniki lahko dodajajo, urejajo ali brišejo.

---

## Funkcionalnosti


### Leti

Na strani **Leti** ima uporabnik dostop do vseh prihajajočih letov:

- Prikaz vseh prihajajočih letov s podrobnostmi, kot so ID leta, čas vzleta, čas pristanka in ID pilota.
- Dodajanje novega leta, vključno s podrobnostmi, kot so  ID leta, čas vzleta, čas pristanka in ID pilota.
- Urejanje obstoječih letov za posodobitev informacij o letu.
- Brisanje letov, ki jih uporabnik ne potrebuje več.

### Zgodovina letov

Na strani **Zgodovina letov** lahko uporabnik pregleda pretekle lete:

- Prikaz zgodovine vseh preteklih letov, vključno s podrobnostmi o letu.
- Urejanje informacij o preteklih letih.
- Brisanje preteklih letov iz evidence po potrebi.

### Letala

Na strani **Letala** lahko uporabnik pregleda in upravlja seznam razpoložljivih letal:

- Prikaz seznama letal z informacijami, kot so ID letala, Ime, Registerska številka, Tip letala.
- Dodajanje novih letal v evidenco.
- Urejanje informacij o obstoječih letalih.
- Brisanje letal, ki niso več na voljo ali niso več v uporabi.

---

## Tehnične zahteve

Za delovanje aplikacije **Evidenca letov** so potrebne naslednje zahteve:

- **Spletni strežnik** (FastAPI)
- **Podatkovna baza** (SQLITE) za shranjevanje podatkov o letih in letalih
- **Programski jezik**: Aplikacija je razvita v Python-u in Javascriptu
- **Odvisnosti**: Knjižnice in paketi, potrebni za zagon aplikacije (navedeni v `package.json`)

---

## Namestitev

1. **Kloniranje repozitorija**: Klonirajte repozitorij z aplikacijo na lokalni računalnik:
    
    ```bash
    git clone <https://github.com/yourusername/EvidencaLetov.git>
    ```
    
2. Zagon frontenda 
    
    ```bash
    cd EvidencaLetov
    cd frontend/evidencaLetenja 
    npm install 
    npm run dev 
    ```
    
3. Zagon backenda
    
    ```bash
    cd EvidencaLetenjaBackend/app
    python main.py
    ```