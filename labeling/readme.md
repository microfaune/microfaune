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

Here are the rules that we use to do the labeling.

- If there are multiple birds singing at the same time: do the labeling as it was a single bird.
- Separate in two labels if there is a silence of more than 2 seconds.
- Don't label bird sounds that are not songs (flapping etc.).
