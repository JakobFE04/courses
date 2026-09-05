Plan for timen:
1. Hva og hvorfor?
2. Induksjon og invarianter
3. Insertion-sort
4. Asymptotisk notasjon

## Skriftlig refleksjon:
Fem personer tar hverandre i hånden. Hvor mange håndtrykk blir det det? Hva med n personer?

$$
 \begin{equation} 
 \sum_{k=1}^{n-1}k \implies \sum_{k=1}^{5-1}k = 1+2+3+4=10
 \end{equation} 
$$
Eller bedre variant$$
 \begin{equation} 
 \frac{n(n-1)}{2} 
 \end{equation} 
$$
Prøvde å ta en sum men var vanskelig å ta hensyn til dobbelt håndtrykk.



# Sortering
Først, om induksjon og invarianter!

Vi vil vise at det blir riktig for alle tilfeller, f.eks. alle inputs.


Vis at P(0)                                                    Grunntilfelle: Vises separat 
Anta P(n-1)                         og vis P(n)        Induksjonssteget
induksjonshypotesen

Sterk induksjon:
Vis P(0)
Anta P(k) for k < n og vis P(n)
P(n) er da sant for alle heltall >= 0

## Bevis oppsummering 
- Invariant: Egenskap som ikke endres
- Initialisering: Invarianten er sann før start
- Vedlikehold: Hvis den er sann før en iterasjon, er den også sann etter
- Terminering: Løkka terminerer, og invarianten gir korrekthet

# Insertion-sort
```bash
for i = 2 to n
	key = A[i]
	j = i - 1
	while j > 0 and A[j] > key
		A[j + 1] = A[j]
		j = j - 1
	A[j + 1] = key
```

# Asymptotisk notasjon
 Hvis vi teller operasjoner, og hver operasjon tar ett mikrosekund, hva rekker vi på et århundre?
![[Pasted image 20260821133758.png]]
Logaritmisk er altså SUPER effektivt, faktoriell er dogshit

## Vi vil ha hvor fort kjøretiden vokser, i grov størrelsesorden
Vi dropper konstanter og lavere ordens ledd
## $\Theta$ notasjon
![[Pasted image 20260821133537.png]]

### Ny oppgave: Utslagsturnering med n deltagere, hvor mange kamper?
Blir n-1 kamper siden må være n-1 tapere og en person forsvinner hver kamp.

# Regning med $\Theta$ 

$$
\Theta(n^2) + n = \Theta(n^2) \ \ \ \& \ \ \\ \Theta(n^2) \cdot n = \Theta(n^3)
$$
![[Pasted image 20260821140134.png]]
Tankegang:
![[Pasted image 20260821140216.png]]


# Hva er lille o og lille $\omega$?
Som før, men for alle c > 0
![[Pasted image 20260821141759.png]]

## NB! Generelt asymmetrisk
![[Pasted image 20260821142125.png]]


# Best/Worst/AVG case
Bruker vanligvis worst-case, avg kan være interessant og best case er uinteressant. 
Avg vil vanligvis være antatt uniform fordeling og ta snitt av det.

NB! Hvis vi vet om vi har best- worst- eller average-case, kan alle tre asymptotiske notasjoner brukes! Om vi ikke vet, må vi velge en notasjon som favner alle muligheter

# Hvordan er dette for insertion sort?
Vi får en øvre og nedre kvadratisk grense, så verste blir $\Theta(n^2)$.

$$
\sum_{i=1}^{n-1} i = n(n-1)/2 = \Theta(n^2)
$$
![[Pasted image 20260821144043.png]]
