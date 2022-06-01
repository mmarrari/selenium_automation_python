# Selenium automation project with python

## Overview
This is a simple example of automating a web browser through selenium and python (intive training)

## Requirements
* Python 3.6+
* docker
* docker-compose
* virtualenv or other virtual environment(pipenv poetry)
* chrome installed

## Usage
To run the example, please execute the following from the root directory:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Main pip packages installed

```
pip install selenium
pip install pytest
pip install webdriver-manager
pip install pytest-docker-compose
```

## Running with Docker Compose

To run the web page example on a Docker container in a background mode, please execute the following from the root directory:

```bash
# building the image
docker-compose up -d
```

The you can access by:

http://localhost:8080/pagina1.html

## Related links

[Selenium](https://www.selenium.dev/)

[docker-compose](https://docs.docker.com/compose/)

[Docker](https://docs.docker.com/)

[XPATH](https://www.w3schools.com/xml/xpath_intro.asp)
