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





# Labeling


## Labeling Tool

Develop Web-based tools to label bird sounds.

Participants: Louis

### Specs

- Spectrogram visualization
- Select part of the sound with a box corresponding to a bird call
- Data output format: SQL DB containing for each box the audio filename, the start timestamp and the end timestamp.
- First step: the easier may be to load audio files manually. Later, we could fetch audio files from where they are stored.

### Tech

- Rails or Django
- SQL DB

## Labeling Task

The labeling task corresponds to the usage of the labeling tool. We should have clear specs and instructions to have a good and homogeneous labeling.

### Specs

- Separate each part of bird sounds
- Don't include other bird sounds (e.g. wing flapping)







# Modeling

## First model from digit recognition

Participants: Patrick

Apply CNN model for digit recognition (audio) to bird datasets.

## First screening

Participants: Florent

Develop a model to reduce labeling time by pre-selecting part of the audio to use for labeling.

The model would have a high False Positive rate (the model thinks that there is bird sound but it's wrong). It would be trained on external datasets.

This first model could be either the model from digit recognition or from Hadrien's replication of Cakir et al. paper (cf. notebook [here](https://colab.research.google.com/drive/1XBNdn98z89HpH2hCqi-bk_fDEQf1SgGA)).

## Model assessement

Participants: Camille

To gain more insights from success and failure it can useful to monitor what our models are doing (cf. [blog post from Andrej Karpathy](https://karpathy.github.io/2019/04/25/recipe/)).








# Denoising

Participants: Louis

## Strategies

Evaluate denoising strategies. Results can be evaluated just listening to denoised data.

## Effects on models

Evaluate denoising strategies on model performance.






# Data Visualization

Participants: Camille

Find compact ways to visualize audio bird data and models performances.

## Labelised Audio Data

- When do they sing (between 5am and 7am)?

Histograms, heatmaps

- Spectrograms corresponding to each bird segment







# Long-Term Storage

Participants: Ysé

## DB

Storage of the Microfaune DB (alternatives with prices).

- For the Bird Audio Detection Challenge, data are stored on Figshare and Archive.

## Model

Back-end hosting for deployment.





# Model Deployment

Participants: Ysé

Several alternatives are considered.

## Upload audio file

A short audio file is uploaded and the label (bird/no bird) is returned.

## Extract bird segments

The user upload an audio file and audio segments containing bird sounds are returned. This can be good first step for bird identification.

## Real-time bird detection

Users turn on their microphone and a visual cue indicate when there is a bird.




# Validation Data

Small part of Microfaune dataset labelised manually. This would be needed for the first-screening model.





# Data Augmentation

Participants: Christian

Add noise from Microfaune audio to bird songs. Test if this leads to better performances.




# Other Ideas

- GAN to generate bird songs

