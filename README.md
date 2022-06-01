# Selenium automation python
This is a simple sample

## Overview
This is a simple example of automating a web browser through selenium and python (intive training)

Features:
- Provide download of a configuration file for the required driver
- List and retrieve existing drivers

## Requirements
Python 3.6+
docker
docker-compose
virtualenv or other virtual environment(pipenv poetry)
chrome installed

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

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t oasis_fastapi .

# starting up a container
docker run -p 8000:8000 oasis_fastapi
```



http://localhost:8080/pagina1.html

## Related links
[Selenium](https://www.selenium.dev/)
https://eagleeyenetworks.atlassian.net/wiki/spaces/~380522518/pages/2038136908/ONVIF+Camera+Integration+System+OASIS

https://eagleeyenetworks.atlassian.net/wiki/spaces/IADP/pages/2509537292/Available+Devices+API
