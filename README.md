<h1 id="about">Weather Buddy API</h1>

API to retrieve basic information about cities weather from [Open Weather Map](https://openweathermap.org/current).

<img src="https://img.shields.io/github/issues/GiovanniDias/weather_buddy_api"/>
<img src="https://img.shields.io/github/stars/GiovanniDias/weather_buddy_api"/>
<img src="https://img.shields.io/github/license/GiovanniDias/weather_buddy_api"/>
<img src="https://img.shields.io/badge/flask-2.0.1-yellow"/>
<img src="https://img.shields.io/badge/docker-blue"/>

<h2 id="table-of-contents">Table of Contents</h2>

* [About](#about)
* [Table of Contents](#table-of-contents)
* [Features](#features)
* [How to use](#how-to-use)
    * [Requirements](#requirements)
    * [Installation](#installation)
    * [Setting Application](#setting-app)
    * [Running Application](#running-app)
        * [Using Flask](#flask-approach)
        * [Using Docker](#docker-approach)
* [Tests](#tests)

<h3 align="center">🚧 Building... 🚧</h3>

<h2 id="features">Features</h2>

- [x] Retrieve city weather info
- [x] Cache retrieved info
- [x] Retrieve cached info
- [x] Unit test
- [x] Endpoint integration tests
- [x] Dockerize application
- [ ] Document endpoints with OpenAPI/Swagger
- [ ] Add OpenAPI/Swagger configuration
- [ ] Deploy on Heroku or AWS EBS

<h2 id="how-to-use">How to use</h2>

<h3 id="requirements">Requirements</h3>
You may need to have installed:

- [Git](https://git-scm.com/downloads)
- [Python 3.9.6](https://www.python.org/downloads/release/python-396/)
- [Docker](https://www.docker.com/products/docker-desktop) e [Docker compose](https://docs.docker.com/compose/install/)

<h3 id="installation">Installation</h3>

[Download Zip](https://github.com/GiovanniDias/weather_buddy_api/archive/refs/heads/master.zip) or use git to clone it using the command

    # https
    $ git clone https://github.com/GiovanniDias/weather_buddy_api/archive/refs/heads/master.zip

    # ssh
    $ git clone git@github.com:GiovanniDias/weather_buddy_api.git

Once you got the source code, it's time to set application virtual environment.

<h3 id="setting-app">Setting application</h3>

*This step is needed for running it in your local machine. If you want to run it using Docker, see [Using Docker](#docker-approach) topic.*

Run the code below to create a virtual environment:

    $ python -m venv/venv

Once created, active it to isolate its context.
    
    # Windows
    $ source venv/Scripst/activate
    
    # Linux / MacOs+
    $ source venv/bin/activate

For now, you may run ```python -m pip install --upgrade pip``` to upgrade pip package version. Then install dependency modules with:

    $ pip install -r requirements.txt

<h3 id="running-app">Running application</h3>

There are the two approaches below to get it running properly.

**<h4 id="flask-approach">Using Flask</h4>**

With venv activated:

    $ flask run -h 0.0.0.0

*This host configuration is needed to allow its endpoints to be reached for other applications in localhost context.*

**<h4 id="docker-approach">Using Docker</h4>**

For running this application with Docker, use:

    $ docker-compose up --build -d
    # or
    $ docker compose up --build -d

depending on Docker version your local machine is using.

<h2 id="tests">Testing application</h2>

To run tests over application, use the command ```pytest``` in root directory.
To run a test specific file use the command below:

    $ pytest tests/FILENAME
