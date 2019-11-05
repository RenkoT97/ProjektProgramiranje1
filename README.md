# Projekt pri predmetu programiranje 1: Analiza iger šaha

Analizirala bom igre šaha. Podatke bom dobila [tu](https://chesstempo.com/game-database.html).

Za vsako igro bom zajela:
* id in datum igre,
* ime, točke po elo ratingu in barvo figur obeh igralcev,
* zmagovalca,
* kraj in dogodek, v katerem se igra odvija,
* število premikov,
* otvoritev.

Hipoteze:
* Ali so igre med igralcema z manj podobnim ratingom krajše?
* Ali lahko ugotovimo stil posameznega igralca (otvoritev, hitrost) in povežemo kakšno lastnost z uspešnejšimi igralci?
* Ali začetna prednost belih figur vpliva na zmago?

Stolpci tabele:
* ID igre
* ocenjeno
* čas začetka igre
* čas konca igre
* število potez
* predaja/mat
* zmagovalec
* vrednost izboljševanja igranja posameznega igralca
* ID belega igralca
* rating belega igralca
* ID črnega igralca
* rating črnega igralca
* vse poteze
* standardna oznaka otvoritve
* otvoritev
* število potez v otvoritve
