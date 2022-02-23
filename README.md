# Flask-restx Boilerplate

Boilerplate for a Flask-restx application

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r etc/requirements.txt
```

## Configuration Variables

Configuration variables exist in the file `etc/settings.json`.
Only the database connection key value pair exists right now.
It can be set to postgres or MySQL.
```bash
{
    "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db"
}
```

## Migrations
To initialize the database, run the following [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/) command

```bash
flask db upgrade
```
## Run

```bash
python3 src/app.py
```

## Pytest
Test cases can be run using the following command

```bash
pytest
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
