# Oracle Cloud Infrastructure Back-end (Django)

## Overview
This project contains a collection of endpoints that are part of an API
hosted on my personal Oracle Cloud Infrastructure (OCI) VM.

## Project Structure
 - mainsite (The main website explaining the project)
 - algodts (Data structures and algorithms endpoint)
     - algos (Algorithm functions)
     - dts (Data structure classes)

## Setting up

To start up the project

```console
python3 -m venv venv
. venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

To stop the project

```console
deactivate
```

To start the project again

```console
. venv/bin/activate
```

## License
This project is licensed under [Apache 2.0](LICENSE).