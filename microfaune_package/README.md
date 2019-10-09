# Package python **microfaune**

## Installation

* Go to the folder *microfaune_package*
* Run the command `pip install .`

### With Pipenv

* Go to the folder *microfaune_package*
* Run the command `pipenv run pip install .`

## Usage

Can be used as any package python:

```python
from microfaune import audio

s, f = audio.load_wav("whatever.wav")
```

To use the detection model:

```python
from microfaune.detection import RNNDetector

detector = RNNDetector()
global_score, local_score = detector.predict_on_wav("whatever.wav")

```


## Documentation generation

Once built, the documentation is available by opening the file `doc/build/html/index.html`.

### Build documentation

To generate the documentation, the packages *sphinx* and *sphinx-rtd-theme* need to be
installed.

All the commands must be launched in console from the folder `doc/`.

To remove the previous generated documentation:
```bash
make clean
```

To generate the html documentation:
```bash
make html
```
