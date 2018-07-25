# Internet Database

Command line interface driven application to save, retrieve and manipulate information about internet domains.

## Getting Started

### Prerequisites

To run this app, you need following pre-installed.

- Python 3.x and pip
    - Pre-installed on most Linux and mac
    - Download from [Python website](https://www.python.org/getit/) for windows

### Installing

- Clone repository

```
git clone https://github.com/ManinderGharuan/internet-db.git
```

- Move to the project directory and install requirements

```
cd internet-db
pip install -r requirements.txt
```

## Deployment

- Commands are listed below

```
python run.py [OPTIONS]
```

- Import domains csv file and save in database

```
python run.py import
```

- Import country csv file and save in database

```
python run.py import-country
```

- Scrap domains from database

```
python run.py scrap
```

- Check status

```
python run.py status
```

## Built With

* [Python](https://www.python.org/) - Python: Programming language

## Authors

* **Maninder Singh Rai** - *Initial work* - [ManinderGharuan](https://github.com/ManinderGharuan)
