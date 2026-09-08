# 1. Veiledet læring
## 1.1 Data
Variabler (statistikk) eller features (maskinlæring) er samme greien.

Kvalitative eller kvantitative variabeler:
- Kvalitative representerer kategorier.
	- Sjanger, aldersgruppe, type frukt ...
- Kvantitative representerer numeriske verdier:
	- Inntekt, alder, antall lyttere, areal, nedbørsmengde, temperatur...

Features benevnes $x_{n}$ 
Targets benevnes $y_{n}$
Indekserer med $(i)$ som slik: $x^{(i)}$
Eksempel Titanic datasett:
![[Pasted image 20260824113923.png]]

Vi vil fjerne hullete data, encode kvalitative variabler og endre størrelsesorden på numeriske verdier. Deretter kan vi se på dataene!



## 1.2 Logistisk regresjon

Enkleste modellen er lineær regresjon:
$$
 \begin{equation} 
 z=\sum_{i=1}^{n}w_{i} x_{i}+b= \mathbf{w} \mathbf{x}+b
 \end{equation} 
$$
Der $\mathbf{w}$ er vektene og $b$ er bias.

Kan gjøres om til sansynlighetsfordeling (mellom 0 og 1) ved å sette inn for #Sigmoid-funksjonen (også kjent som #aktiveringsfunksjon)
$$
 \begin{equation} 
 \sigma(z)= \frac{1}{1+e^{-z}} \implies y_{pred}= \frac{1}{1+e^{-(\sum_{i=1}^{n}w_{i} x_{i}+b)}}
 \end{equation} 
$$

### 1.2.1 Trening og tapsfunksjon
Funksjonen som brukes til å beregne målopnnåelse kalles for #tapsfunksjon. Forteller hvor nærme modellens prediksjon er den riktige verdien, eller target:
$$
 \begin{equation} 
 \mathcal{L}(y_{pred},y)
 \end{equation} 
$$
Den tar inn modellprediksjonene $y_{pred}$ og #targets $y$. **NB!** må være deriverbar (se [[#1.2.2 Gradient descent]])
[Eksempel link](https://www.geeksforgeeks.org/machine-learning/ml-common-loss-functions/)
Eksempel på funksjon for klassifisering av binær target:
$$
 \begin{equation} 
 {L}(y_{pred},y) = y_{pred}^y(1-y_{pred})^{1-y} 
 \end{equation} 
$$
$$
 \begin{equation} 
 \implies{L}(\mathbf{w},b|x,y)=\sigma(\mathbf{wx}+b)^y(1-\sigma(\mathbf{wx}+b))^{(1-y)} 
 \end{equation} 
$$
Vi vil finne en #likelihood og ikke en sannsynlighet fordi vi **ikke** har lyst til å endre dataene slik at sannsynligheten for target endrer seg. men heller endre modellen slik at den estimerte sannsynligheten passer med den virkelige (target).

Vi ønsker å ha likelihood for å estimere riktig være maksimal, så vi kan legge til et minustegn på tapsfunksjonen for å minimere denne. Vi bruker gjerne å ta logaritmen av av likelihood for å få **log-likelihood** (Minimere tap == maksimere Likelihood). Dette kalles for #cross-entropy-loss.

Eksempel på tapsfunksjon: #binary_cross-entropy-loss
Vektet tapsfunksjon: Maksimere likelihood for riktig kategorisering av dataene
$$
 \begin{equation} 
 \mathcal{L}(y_{pred},y)=-\omega_{1}y\ln y_{pred}-\omega_{0}(1-y)\ln(1-y_{pred}) 
 \end{equation} 
$$
Der $\omega_{0}$ og $\omega_{1}$ er vekter for klassene, se [[#Vektet tapsfunksjon]]. 
y er target og vi kan bruke $y_{pred}$ fra [[#1.2 Logistisk regresjon|formelen her]].

Vi kan nå skrive om modellen definert av parametrene $\mathbf{w}$ og $b$ for å finne parametrene som minimerer tapet i gjennomsnitt over alle datapunktene ($x$). Dette kaller vi for å **trene modellen**. Vi får da at vi skal maksimere log-likelihooden for parametrene som vi definerer:
$$
 \begin{equation} 
 \theta=(\mathbf{w},b) \implies \hat{\theta}=arg_{\theta} \min \frac{1}{N} \sum_{i=1}^{N} \mathcal{L}(f(\mathbf{x}^{(i)};\theta),y^{(i)})
 \end{equation} 
$$
Detta kalles **conditional maximum likelihood estimation**, og kan løses med bruk av [[#1.2.2 Gradient descent|gradient descent]].

### 1.2.2 Gradient descent
Når vi ser på funksjonen vår beveger vi oss i rommet spent ut av verdiene $\theta$, fire verdier gir et fire dimensjonalt rom. Vi vil finne minimumspunktet til funksjonen uten at vi kjenner formen til den. **NB!** så lenge tapsfunksjonen er konveks, så vil vi alltid kunne finne lokalt minium med gradienten.

I starten av treningen har alle parametrene en tilfeldig verdi, og vi oppdaterer verdiene iterativt, gjennom flere steg. Gradienten til tapsfunksjonen peker i retning av økende tap, og siden vi ønsker å minke tapet må vi bevege oss i motsatt retning. Dette representerer vi gjennom et minustegn, og regelen for parameteroppdateringen kan skrives som følger:
$$
 \begin{equation} 
 \theta^{t+1}=\theta^t - \eta  \frac{\partial}{\partial \theta} \mathcal{L}(f(\mathbf{x};\theta),y)
 \end{equation} 
$$
Der $\eta$ er #læringsraten, som bestemmer hvor mye hvert steg $t$ skal korrigere til parameterverdien. **NB!** $\eta$ eller læringsraten er en parameter for å justere treningen til modellen, men er **ikke** en del av modellen! Dette kaller vi for en #hyperparameter, som definerer læringsprosessen, men ikke modellen. Den kan vi leke med/justere mye for å optimalisere, men generelt ønsker små steg for å ikke hoppe over minimumspunktet men også ikke fordi da vil modellen bruke lang tid på å læres.

Framgangsmåten vil da bli å finne gradienten av tapsfunksjonen, med hensyn til vær av parametrene. Eksempel med titanic modellen:
![[Pasted image 20260824123129.png]]


### 1.2.3 Trening
En måte å strukturere #læringsalgoritme på:

```python

class LogisticRegression: 
	def __init__(self, learning_rate=0.1, epochs=1000): 
		self.learning_rate = learning_rate 
		self.epochs = epochs 
		self.weights, 
		self.bias = None, None 
		self.losses, self.train_accuracies = [], []

	def sigmoid_function(self, x): 
	
	def _compute_loss(self, y, y_pred): 
	
	def compute_gradients(self, x, y, y_pred): 
	
	def update_parameters(self, grad_w, grad_b): 
	
	def accuracy(true_values, predictions): 
		return np.mean(true_values == predictions)

def fit(self, x, y): 
	self.weights = np.zeros(x.shape[1]) #x.shape = datapunkter, features 
	self.bias = 0 

	# Gradient Descent 
	for _ in range(self.epochs): 
		lin_model = np.matmul(self.weights, x.transpose()) + self.bias 
		y_pred = self._sigmoid(lin_model) 
		grad_w, grad_b = self.compute_gradients(x, y, y_pred)
		self.update_parameters(grad_w, grad_b) 
		
		loss = self._compute_loss(y, y_pred) 
		pred_to_class = [1 if _y > 0.5 else 0 for _y in y_pred] 
		self.train_accuracies.append(accuracy(y, pred_to_class)) 
		self.losses.append(loss) 

def predict(self, x): 
	lin_model = np.matmul(x, self.weights) + self.bias 
	y_pred = self._sigmoid(lin_model) 
	return [1 if _y > 0.5 else 0 for _y in y_pred]
```

Når skal bruke koden, bør en **ikke** bruke hele datasettet til å trene modellen. Del dataen opp i #testdata og #treningsdata. Treningsdataene brukes til parametertilpasning, mens testdataene ikke røres før modellen er ferdig tilpasset, og brukes for å evaluere modellen før denne tas i bruk. Bruk gjerne $\texttt{train\_test\_split}$ fra biblioteket $\texttt{scikit-learn}$.

Eksempel på kjøring av kode: 
```python 
# Training 
train_epochs = 30 

# Initialize and train the model 
log_reg = LogisticRegression_(learning_rate=0.01, epochs=train_epochs) log_reg.fit(X_train, y_train) 

# Make predictions 
predictions = log_reg.predict(X_test)

``` 


### 1.2.4 Evaluering
Lurt å plotte tapet (loss) mot treffsikkerhet (accuracy) for å se treningsprosedyren er god.
![[Pasted image 20260824130912.png]]

Mange metrikker baseres på #confusion_matrix som brukes ofte for å evaluere klassifiseringsmodeller. 
![[Pasted image 20260824131050.png]]

Dette kan vi bruke til å regne ut flere matrikker som i tabellen under:
![[Pasted image 20260824131036.png]]


### 1.2.5 Klassifiseringsterskel
Enkel måte å justere på klassifiseringsterskelen er å endre linjen i $\texttt{fit}$ og $\texttt{predict}$ funksjonene:
$$
 \begin{equation} 
 \texttt{[1 if \_y > K else 0 for \_y in y\_pred]}
 \end{equation} 
$$
Der $\texttt{K}$ er klassifiseringsterskelen. Hvis en vil være sikker på at modellens predikasjon er riktig, vil en velge en høyere verdi for klassiferingsterkselen som 0.7. 

Det er vanlig å plotte **FPR** (False Positive Rate) og **TPR** (True Positive Rate) som funksjon av klassifiseringsterskelen. Dette gir oss **Receiver Operating Characteristic** ( #ROC)- kurven. Området under kurven til ROC kaller vi for #AUC (area under curve) som vi ønsker skal være større enn 0.5 (tilsvarer tilfeldig gjetting). ROC AUC representer sannsynligheten for at modellen vil predikere en høyere verdi for et tilfeldig valgt posititvt datapunkt enn for et tilfeldig valgt negativt datapunkt. 
![[Pasted image 20260824133106.png]]
Ingen tradeof mellom TPR og FPR, men alltid en tradeoff med metrikkene en ønsker å ha høy:
 - En annen vanlig kurve å studere er den som viser precision (TPR) og recall (PPV). 
![[Pasted image 20260824133534.png]]
Presisjon: Angir andel korrekt predikert positive per predikert positiv.
 - Høy presisjon svarer til lavt relativt antall falske alarmer.
 - Viktig om falske alarmer er dyrt, som å rykke ut til brann.

Recall: Angir andell korrekt predikert positive per totalt psoitive.
- Høy recall svarer til lavt antall missed cases.
- Viktig om kritisk å ikke treffe på en case, som med detektere kreft.

### 1.2.6 Kort om entropi og cross entropy loss
![[Pasted image 20260824133721.png]]

Hvis vi sammenligner dette med #tapsfunksjon og #cross-entropy-loss , ser vi at den ene sannsynlighetsfordelingen representerer labels i datasettet, mens den andre representerer modellens prediksjoner. Tapsfunksjonen forteller oss altså om forskjellen mellom de to fordelingene, og siden målet vårt er å lage en klassifiseringsmodell, ønsker vi at forskjellen mellom de to fordelingene er minst mulig. Vi kan generalisere utrykket over til: 
$$
 \begin{equation} 
  \mathcal{L}(\hat{y},y)=-\sum_{i}^{}y_{i}\log(\hat{y}_{i}),
 \end{equation} 
$$
hvor summen går over alle klassene $i$.

### 1.2.7 Bayes' teorem
Vi kan bruke Bayes' teorem til å regne: 
$$
 \begin{equation} 
 p(C_{k}|x)=\frac{p(x|C_{k})p(C_{k})}{p(x)} 
 \end{equation} 
$$
Vi får da at:
- $p(C_{k})$ er $a\  priori$ sannsynligheten for klasse, altså fordelingen av klassene i treningsdataene. Denne omtales som prior, fordi det er sannsynligheten for **klassetilhørighet** vi kan estimere uten å vite noe om det aktuelle datapunktet (legg merke til at $x$ ikke forekommer i dette leddet). 
- $p(x)$ er fordelingen av selve dataene, uavhengig av klasse (legg merke til at $C_{k}$ ikke forekommer i dette leddet). Dette er den faktiske sannsynlighetsfordeligen av alle feature-verdiene for alle dataene, og den har like mange dimensjoner som datasettet har features. Dette leddet omtales som evidens. 
- $p(x|C_k)$ er den betingede sannsynlighetsfordelingen av dataene gitt klassen, og det er en likelihood. Det er altså en egen sannsynlighetsfordeling – med like mange dimensjoner som datasettet har features – for hver klasse.

Vi kan regne $p(C_{k})$, og for titanic casen kan vi se at $p(x)$ vil være vanskelig å bergne, men at den bidrar like mye til begge klassene så vi kan se vekk i fra den og få at:
$$
 \begin{equation} 
 p(C_{k})  ∝ p(x|C_{k})p(C_{k})
 \end{equation} 
$$

Hvis vi antar at verdiene til featuresene er uavhengige av hverandre for alle features, så kan vi skrive dette om til Naiv Bayes:
$$
 \begin{equation} 
 p(C_{k}|x) ∝ p(C_{k}) \prod_{i=1}^{n}p(x_{i}C_{k})
 \end{equation} 
$$
Som gir at den tilsvarende sannsynligheten for klassetilhørighet:
$$
 \begin{equation} 
 \hat{y}= \arg_{k\ \epsilon [1,\dots,n]} \max p(C_{k}) \prod_{i=1}^{n}p(x_{i}C_{k})
 \end{equation} 
$$


### 1.2.8 Dimensjonsforbannelsen

**FINN NOTATER HER**


### 1.2.9 Trening på ubalansert data
Om vi har mye flere datapunkter for forskjellige klasser, ender vi opp med å få **underrepresentert** og **overrepresentert** klasser. Hvis forskjellen mellom klasser blir for stor, vil modellen belønnes om den bare predikerer at alle datapunktene tilhører den overrepresenterte klassen som gir en dårlig modell. For å justere skjevfordelingen mellom klassene kan vi endre på klassifiseringsterskelen som i utrykket:

$$
 \begin{equation} 
 \texttt{y\_{pred = [1 if \_y > K=0.5 else 0 for \_y in y\_pred]}}
 \end{equation} 
$$
fra 0.5 til en verdi som gir modellen høyere verdi på de andre metrikkene. Kan bruke precision-recall plottet som et ugangspunkt. Å maksimere en metrikk kommer på bekostning av andre metrikker og å justere terkselen forbedrer **ikke** modellen: det endrer kun hvordan vi forholder oss til modellens prediksjoner. Vi kan også endre dataene eller tapsfunksjonen.

#### Resampling
##### Undersampling: 
Her trekker vi like mange datapunkter fra den overrepresenterte klassen som vi har tilgjengelig i den underrepresenterte klassen. Da ender vi opp med et datasett bestående av like mange datapunkter fra hver klasse, men potensielt veldig få datapunkter totalt. Dette kan føre til at modellen som trenes på dataene undertilpasser (underfit).
##### Oversampling:
Her kopierer vi instanser fra den underrepresenterte klassen, inntil vi har like mange datapunkter fra den underrepresenterte som fra den overrepresenterte klassen. Da ender vi også opp med like mange datapunkter fra hver klasse, men potensielt mange duplikater fra den underrepresenterte klassen. Dette kan føre til at modellen som trenes på dataene overtilpasser (overfit)

#### Vektet tapsfunksjon
Vi kan også fortelle modellen hvilken av klassene som er ekstra viktig ved å straffe feilprediskjoner (høyere tap) på den viktige klassen, relativt til de andre klassene. F.eks med #binary_cross-entropy-loss. Vi ser at for de to leddene, bidrar kun det første leddet til tapet når y=1 og det andre leddet når y=0. Ved å sette inn vektene $w_{1} \ \& \ w_{0}$ for henholdsvis første og andre leddet kan vi gjøre at feilprediksjoner for den ene vil gi ut høyere tap enn den andre.


## 1.3 Beslutningstrær
### 1.3.1 Noder
#Root-node eller rotnoden er starten på beslutningstreet av dataene med alle featuresene som er splittet i en trestruktur. 

Under har vi beslutningsnoder (de)cision nodes) som begge har kriterier for å splitte dataene (splitting criteria). Alle noder som splitter dataene er enten rotnoden eller beslutningsnoder. 

Nederst i treet er løvnodene (leaf nodes) som ikke splitter dataene, som inneholder predikert verdi for datainstansen som ble sendt gjennom treet.

Beslutningstrær består av trestumper (tree stumps) som igjen består av en rotnode og $n$ løvhoder, for $n$ mulige utfall.

Treningsdataene brukes for å finne ut hvilke trestumper (og tilhørende beslutningskriterier) som bør settes sammen for å lage treet. N˚ar vi bygger beslutningstrær ønsker vi alltid å velge det splitt-kriteriet som lar oss ta beslutningen tidligst mulig, altså reduserer usikkerheten mest mulig. Redusert usikkerhet er endringen i usikkerhet etter sammenliknet med før splitt. I hovedsak brukes følgende tre metrikker for å måle hvor mye et splitt-kriterium (feature og verdi) reduserer usikkerheten:
- Log loss (Se #tapsfunksjon og #cross-entropy-loss)
- Gini impurity
- Entropi

### 1.3.2 Gini impurity
Gini-urenheten er et tall i \[0, 0.5] som angir sannsynligheten for at et nytt, tilfeldig datapunkt feilklas- sifiseres hvis det gis et tilfeldig label i henhold til klassedistribusjonen i datasettet. Gitt et datasett D bestående av datapunkter fra k klasser, med sannsynlighet pi for at en instans tilhører klassen i ved en gitt node, er datasettets Gini-urenhet:
$$
 \begin{equation} 
 \text{Gini}(D)=1-\sum_{i=1}^{k} p_{i}^2 
 \end{equation} 
$$
Intuitivt: Du har en pose med kuler i ulike farger, hvor farge representerer klasse. Gini-urenheten måler hvor sannsynlig det er at du gjetter feil farge på en tilfeldig trukket kule, hvis du gjetter at kulens farge følger distribusjonen av farger i posen.
**Lav Gini-urenhet** representerer scenariet der de fleste kulene har samme farge, slik at det er lav sannsynlighet for å gjette feil farge på en tilfeldig trukket kule. Datasettet regnes da å ha lav urenhet. 
**Høy Gini-urenhet** representerer motsatt scenario, der klassene er forholdsvis likt representert, og det er høy sannsynlighet for å gjette feil farge på en tilfeldig trukket kule. Datasettet regnes da å ha høy urenhet.

Hvis dataset $D$ splittes på feature $f$ til to subsett $D_{1}$ og $D_{2}$ med henholdsvis $n_{1}$ og $n_{2}$ datapunkter, har vi 
$$
 \begin{equation} 
 \text{Gini}_{f}(D) = \frac{n_{1}}{n}\text{Gini}(D_{1}) + \frac{n_{2}}{n}\text{Gini}(D_{2}) 
 \end{equation} 
$$
### 1.3.3 Entropi
Gitt en sannsynlighetsfordeling over $k$ klasser, er sannsynligheten for hver klasse $p_{i}$. Entropien til fordelingen er da gitt ved:
$$
 \begin{equation} 
 I(p_{1},\dots,p_{k}) = - \sum_{i=1}^{k} p_{i}\log_{2}(p_{i}) 
 \end{equation} 
$$
![[Pasted image 20260908112207.png]]

### 1.3.4 Bygge beslutningstrær
For å bygge beslutningstrær brukes som oftest biblioteket $\texttt{sklearn.DecisionTreeClassifier}$. Den lar en velge mellom de splitt-kriteriene Gini impurity, entropy og log loss.

Gini impurity og entropy er oppfører seg likt, hovedforskjellen er entropy har en ekstra logaritme i kjøretid. Gini impurity er mindre beregningstungt og default i $\texttt{sklearn.DecisionTreeClassifier}$. 

Utover valg av beslutningskriterier, må vi bestemme:
- Når skal vi slutte å splitte, selv om nederste node har instanser fra begge klassene?
- Hva gjøres med løvnoder med instanser fra begge klassene?
Kan oppstå for 3 tilfeller vi må slutte å splitte:
1. Når det ikke finnes flere features å splitte på. Dvs har splittet på alle tilgjengelige features, men har ikke laget løvnoder som tilordner alle treningsdatapunktene til riktig klasse.
2. Når det ikke finnes flere datapunkter å teste. Alle kombinasjoner av features som er **tilgjengelig i dataene** har blitt testet, men alle tenkelige kombinasjoner av features ikke er testet.
3. Når treet har nådd en predifinert maksimal dybde fra hyperparameter vi velger før begynner å bygge treet.

Etter at treet er bygget vil vi sannsynligvis ha løvnoder som inneholder treningsdatapunkter fra begge klasser. For å bestemme hvilken beslutning en slik node kan ta har vi flere muligheter, hvorav de vanligste er å returnere:
1. Den dominante klassen i noden, altså label tilsvarende den dominante klassen fra treningsdataene i løvnoden.
2. Et tilfeldig trukket label fra treningsdataene, altså **a priori**-sannsynligheten.

![[Pasted image 20260908114711.png]]


## 1.4 Regresjon
### 1.4.1 Data og tapsfunksjon
Prediksjon til kontinuerlige verdier kalles **regresjon**. Generelt: estimering av en (eller flere) kontinuerlige verdier. Enkleste tilfellet er lineære regresjonsmodellen:
$$
 \begin{equation} 
 f(x)=\beta_{0}+\beta_{1}x_{1}+\beta_{2}x_{2}+\dots \beta_{n}x_{n} 
 \end{equation} 
$$
Kan bruke igjen mye av kode fra klassifisering, og har igjen en bias $\beta_{0}$ og vekter/parameter $\beta_{i}$ for hver dataegenskap $x_{i}$. Vi bruker igjen #gradient_descent for å optimalisere parametrene.

Vanligste tapsmodellen innen regresjon er #mean_squared_error:
$$
 \begin{equation} 
 \text{MSE} = \frac{1}{2N} \sum_{i=1}^{N}[y^{(i)}-f\mathbf({x}^{(i)})]^2 
 \end{equation} 
$$
Her er $y^{(i)}$ er target for datapunkt $\mathbf{x}^{(i)}$, f er modellen og summen (gjennomsnittet) går over alle N instansene (radene) i datasettet. Liten MSE gir god prediksjon og stor gir dårlig. Gradient descent for et datasett med en feature $x_{1}$ gir oss:

$$
 \begin{equation} 
 \frac{\partial\mathcal{L}}{\partial \beta_{0}} = \frac{1}{N}\sum_{i=1}^{N}(\beta_{1}x^{(i)}+\beta_{0}-y^{(i)})
 \end{equation}
$$
$$
 \begin{equation} 
  \frac{\partial\mathcal{L}}{\partial \beta_{1}} = \frac{1}{N}\sum_{i=1}^{N} x^{(i)}(\beta_{1}x^{(i)}+\beta_{0}-y^{(i)})
 \end{equation} 
$$
Oppdateringsregel til parametrene i regresjonsmodellen blir da:
$$
 \begin{equation} 
 \beta_{0}\leftarrow \beta_{0} -   η \frac{1}{N}\sum_{i=1}^{N}(f(x^{(i)})-y^ {(i)}) \ \ \ \beta_{1} \leftarrow \beta_{1} - η \frac{1}{N}\sum_{i=1}^{N} x^{(i)} (f(x^{(i)})-y^ {(i)})
 \end{equation} 
$$
