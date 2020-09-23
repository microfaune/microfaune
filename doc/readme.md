# Review

## Litterature

Scientific papers or blog articles on Bird Detection.

### Papers from the Bird Audio Detection Challenge

- [Cakir et al.](http://ieeexplore.ieee.org/document/8081508/)

- [Thakur et al.](http://ieeexplore.ieee.org/document/8081510/)

- [Kong et al.](http://ieeexplore.ieee.org/document/8081509/)

- [Pellegrini](http://ieeexplore.ieee.org/document/8081506/)

- [Adavanne et al.](http://ieeexplore.ieee.org/document/8081505/)

- [Grill and Schlüter](http://ieeexplore.ieee.org/document/8081512/)

- [Abrol et al.](http://ieeexplore.ieee.org/document/8081510/)

### Others

[Google Audio AI](https://ai.google/research/pubs/pub45611)

## DB

- Datasets using our microphone (Swift from the Cornell Lab).

## Labeling Tools

What tool could be used to do the labeling (bird/no bird)?

- [CrowdCurio - audio annotator](https://github.com/CrowdCurio/audio-annotator)
- [EchoML](https://github.com/ritazh/EchoML)
- [BAT](https://github.com/BlaiMelendezCatalan/BAT)

## Other

### General Tips To Run A Deep Learning Project

[Great insights from Andrej Karpathy (director of AI at Tesla)](https://karpathy.github.io/2019/04/25/recipe/). I think we should read it several time along the project :)

### AI For Audio

[Issue of using spectrograms as inputs of CNN](https://towardsdatascience.com/whats-wrong-with-spectrograms-and-cnns-for-audio-processing-311377d7ccd
)



# Validation Data

Small part of Microfaune dataset labelised manually. This would be needed for the first-screening model.



# Other

- GAN to generate bird songs
- AI For Audio: Issue of using spectrograms as inputs of CNN
- Identification step ideas:

Extract birds sounds from scraping xeno-canto (code and csv on GitHub)
Apply basic CNN (WIP) first to recognize sounds, then why not, species or maybe Families?
improvements:
Visualization, start with little clean data, understand typical time zones, birds frequencies, etc.
Test multiple kinds of pre-processings
Reach proper overfitting first
Detect birds first (preliminary NN)
Try scraping specifically bird sounds (and not wings or other stuff)
End purpose: test it on our cité U soundtrack, maybe help labelling by pre-sorting families, etc.


# Bioacoustique

Thierry Aubin, chercheur bioacousticien
quel son un oiseau reconnaît comme son propre chant ?
module le chant à partir d’un chant enregistré (change la fréquence, l’intensité etc) et identifie le moment où on ne le reconnaît plus
https://www.researchgate.net/profile/Thierry_Aubin
http://neuro-psi.cnrs.fr/spip.php?article98

Hervé Glotin, chercheur bioacousticien, spécialiste deep learning
Reconnaissance automatique d’espèce (oiseaux, cétacés),
Localisation et tracking par acoustique passive
http://glotin.univ-tln.fr/
https://www.researchgate.net/profile/Herve_Glotin






