# pythonbible-api

An API wrapper for the [pythonbible](https://github.com/avendesora/pythonbible) library using [FastAPI](https://fastapi.tiangolo.com/).

[![PyPI version](https://img.shields.io/pypi/v/pythonbible-api?color=blue&logo=pypi&logoColor=lightgray)](https://pypi.org/project/pythonbible-api/)
[![license MIT](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)

<!--![Test](https://github.com/avendesora/pythonbible-api/workflows/Test/badge.svg)-->
![CodeQL](https://github.com/avendesora/pythonbible-api/workflows/CodeQL/badge.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1139536debca4c0894aefa1fa8324a8e)](https://app.codacy.com/gh/avendesora/pythonbible-api?utm_source=github.com&utm_medium=referral&utm_content=avendesora/pythonbible-api&utm_campaign=Badge_Grade_Settings)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/8f7407c1b98040e185b81c945b78de22)](https://www.codacy.com/gh/avendesora/pythonbible-api/dashboard?utm_source=github.com&utm_medium=referral&utm_content=avendesora/pythonbible-api&utm_campaign=Badge_Coverage)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Python 3.9](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue?logo=python&logoColor=lightgray)](https://www.python.org/downloads/)

> **WARNING**: This is very much still a work in progress and does not yet have a
> stable release. Breaking changes are expected.

## Installation

```shell script
pip install pythonbible-api
```

## Usage

To test pythonbible-api out locally, install uvicorn.

```shell script
pip install uvicorn[standard]
```

Run the following command in the ``pythonbible_api`` directory to start uvicorn:

```shell script
uvicorn main:app --reload
```

Uvicorn should now be running locally at [http://127.0.0.1:8000](http://127.0.0.1:8000/), and you can view the documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).
