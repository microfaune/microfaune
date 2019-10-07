
# Data Visualization

Participants: Camille

Find compact ways to visualize audio bird data and models performances.

## Labelised Audio Data

- When do they sing (between 5am and 7am)?

Histograms, heatmaps

- Spectrograms corresponding to each bird segment

## Bilan de l'observation spectrogramme

Rien de significatif au dessus de 15kHz
pour un spectogramme le plus propre possible
fenetre de FFT de 20ms
overlap de 50%
durée de 10s, fenêtre de 20 sur 5
à voir si on peut réduire ensuite

pour le linéaire
overlap ne joue que sur l'échelle du temps
nfft augmente le nbre de points en fréquence et réduit le nbre de point en temps

pour le mel
overlap ne joue que sur l'échelle du temps
nfft réduit le nbre de point en temps
MEL donne le nbre de points en fréquence

reste à faire : 
lire un fichier mp3



NB ! Martellement du pic épeichette
 et roucoulement du pigeon/tourterelle, échelle log plutôt ??



