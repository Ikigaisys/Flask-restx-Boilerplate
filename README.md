# Flask-restx Boilerplate

Boilerplate for a Flask-restx application

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r etc/requirements.txt
```

## Configuration Variables

Configuration variables need to be in the file `etc/settings.json`. **Please create this file.**
Only the database connection key value pair exists right now.
It can be set to postgres or MySQL.
#### Example `settings.json`
```bash
{
    "env": "dev",
    "sqlalchemy_database_uri": "sqlite:////absolute/path/to/project/test.db"
}
```

## Migrations
To initialize the database, run the following [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html#running-our-first-migration) command

```bash
cd src/model
alembic upgrade head
cd ../..
```
## Run

```bash
python3 src/app.py
```
**Open the URL http://127.0.0.1:5000/api/v1/**


## Pytest
Test cases can be run using the following command

```bash
pytest
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
