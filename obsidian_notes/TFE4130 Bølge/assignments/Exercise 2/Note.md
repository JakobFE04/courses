At den tidsmidlede intensiteten kan skrives som $\overline{I} = \frac{1}{2} \text{Re}\{p \cdot v^*\}$ er en veldig nyttig matematisk snarvei i bølgeforplantning.

Her er den trinnvise forklaringen på hvorfor det blir slik, basert på hintene i oppgaven:
1. Definisjonen med reelle tall
Den fysiske, øyeblikkelige intensiteten er alltid produktet av de reelle signalene:
$$I(t) = \text{Re}\{p(t)\} \cdot \text{Re}\{v(t)\}$$
For en harmonisk bølge med vinkelfrekvens $\omega$ kan de komplekse størrelsene skrives som:
$p(t) = P_0 e^{j\omega t}$ (hvor $P_0$ er den romlige delen $(B/r)e^{-jkr}$)
$v(t) = V_0 e^{j\omega t}$ (hvor $V_0$ er den romlige delen)
2. Triangulering ved hjelp av Hint 2
Hint 2 sier at realdelen til et komplekst tall $Z$ kan skrives som:
$$\text{Re}\{Z\} = \frac{1}{2}(Z + Z^*)$$
Bruker vi dette på de to reelle leddene våre, får vi:
$$\text{Re}\{p(t)\} = \frac{1}{2}(p + p^*) = \frac{1}{2}(P_0 e^{j\omega t} + P_0^* e^{-j\omega t})$$
$$\text{Re}\{v(t)\} = \frac{1}{2}(v + v^*) = \frac{1}{2}(V_0 e^{j\omega t} + V_0^* e^{-j\omega t})$$
3. Multiplikasjon (De 4 leddene fra Hint 3)
Når vi Ganger sammen $\text{Re}\{p(t)\}$ og $\text{Re}\{v(t)\}$, får vi totalt fire ledd:
$$I(t) = \frac{1}{4} \left[ P_0 V_0 e^{j2\omega t} + P_0 V_0^* + P_0^* V_0 + P_0^* V_0^* e^{-j2\omega t} \right]$$
4. Tidsmidling (Integrasjon)
Når vi skal finne den tidsmidlede intensiteten $\overline{I}$, integrerer vi over en hel periode $T$. Som beskrevet i Hint 3:
Leddene med tidsavhengighet, $e^{j2\omega t}$ og $e^{-j2\omega t}$, svinger harmonisk opp og ned. Gjennomsnittet av en ren sinus/cosinus-bølge over en hel periode er lik 0.
De to midterste leddene, $P_0 V_0^*$ og $P_0^* V_0$, er helt konstante over tid fordi tidsavhengigheten ($e^{j\omega t} \cdot e^{-j\omega t} = 1$) ble kansellert.
Etter tidsmidlingen står vi derfor bare igjen med de to konstante leddene:
$$\overline{I} = \frac{1}{4} \left[ P_0 V_0^* + P_0^* V_0 \right]$$
5. Tilbake til Realdelen
Siden $P_0^* V_0$ er den komplekst konjugerte av $P_0 V_0^*$, kan vi bruke regelen fra trinn 2 baklengs:
$$(P_0 V_0^*) + (P_0 V_0^*)^* = 2 \cdot \text{Re}\{P_0 V_0^*\}$$
Setter vi dette inn, får vi:
$$\overline{I} = \frac{1}{4} \cdot 2 \cdot \text{Re}\{P_0 V_0^*\} = \frac{1}{2} \text{Re}\{P_0 V_0^*\}$$
Siden tidsleddet uansett blir kansellert ($e^{j\omega t} \cdot e^{-j\omega t} = 1$), er dette matematisk identisk med å skrive:
$$\overline{I} = \frac{1}{2} \text{Re}\{p(t) \cdot v^*(t)\}$$
