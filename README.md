# Cloud Computing Project - Fake News - Crawler

## Requirements

- Python3.6+

## Installation

It's advisable to create a virtual environment with python (optional):

```sh
python -m venv venv
source venv/bin/activate
```

First install all dependencies:

```sh
pip install -r requirements.txt
```


To run a spider, first create a folder at the root of the project to host the collected data:
```sh
mkdir <spider_name>_data
```

Then run the scrapy command to start the processus:
```sh
scrapy crawl <spider_name>_data
```

The available spider_name are the followings:
- `lefigaro` (Le Figaro)
- `francheinfo` (Franche TV Info)
- `legorafi` (Le Gorafi)
- `lemonde` (Le Monde)
- `mediaspress` (Medias Presse Info)
- `nouvelobs` (Le Nouvel Observateur)



