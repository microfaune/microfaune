# Background

Biodiversity evaluation and monitoring is the first step toward its protection. The goal of the Microfaune project is to evaluate avifauna in Cité Universitaire park (Paris, France) from audio recordings.

![swift](images/swift.jpg)

The aim is to provide the scientific community with a labeled database (bird/no-bird) and to develop machine learning algorithms for bird audio detection. The project includes also the creation (from scratch or using existing tools) of web-based tools to label and visualize bird sounds.

The goal is to advance leverage state of the art research and contribute to open data in the field.

# Skills

You have or want to acquire any of these skills:

- Machine Learning
- Deep Learning (CNN, RNN...)
- Web Development
- Transfer Learning
- Signal Processing
- Data Engineering
- Audio processing
- Ecological interest
...

# Roadmap

Here is a tentative roadmap (to be challenged!):

![roadmap](images/roadmap.png)

# Getting Started

## Audio Tutorial

![spectrogram](images/spectrogram_example.png)

Since we'll work on audio data, it should be useful to have notions on basic operations on audio. We provide an introductory notebook showing how to load audio data, listen to it in the notebook, plot waveforms, calculate spectrograms, etc.

Here is a [notebook](https://github.com/hadrienj/microfaune/blob/master/getting_started.ipynb) to getting started! Feel free to contribute and improve this notebook if you see anything that you think is missing.

## Knowledge Sharing

Let's try to define the setup we'll need and try to have a homogeneous workspace to make collaboration easy (and remote work possible). Here's my take (to be challenged as well :) ):

- Using pipenv to create virtual environments
- Using Git/Github to collaborate
- Using Jupyter notebook (local and Google Colab)
- Understand audio data and possibilities (cf. Audio Tutorial)

# External Data

If you look on the roadmap, you should see some sub-projects using external data. These data are audio files labelised with the presence or absence of bird. There are at least two databases:

- Warblr
- FreeField1010

Some ideas can be tried on these data making easy comparison of performances.

You can find these databases [here](http://machine-listening.eecs.qmul.ac.uk/bird-audio-detection-challenge/).

# Wazo Data

Wazo Data are data from recordings in Cité Universitaire in Paris. All data is not yet accessible (but will be soon). As for now, around 5h of data is available to kick start the project.


