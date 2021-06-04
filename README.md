# Aineopintojen harjoitustyö: tietorakenteet ja algoritmit

Aineopintojen harjoitustyö: tietorakenteet ja algoritmit, Helsingin yliopisto

Lab project: data structures and algorithms, University of Helsinki

### Weekly reports (in Finnish)
- [Week 1](docs/week_reports/w1.md)
- [Week 2](docs/week_reports/w2.md)
- [Week 3](docs/week_reports/w3.md)
- [Week 4](docs/week_reports/w4.md)
- Week 5
- Week 6

### Documentation
- [Requirement specification](docs/requirements.md)
- [Installation guide](docs/installation_guide.md)
- [User manual](docs/user_manual.md)
- [Testing document](docs/testing_document.md)
- [Implementation document](docs/implementation_document.md)

### Known issues
[Check the issues in GitHub](https://github.com/roopekole/tira-labra/issues)

### Get started

See [Installation guide](docs/installation_guide.md) for more details

See [User manual](docs/user_manual.md) for using the application

1. Initiate the virtual environment
```bash

python -m venv venv

source venv/Scripts/activate
```



2. Install dependencies:


```bash

pip install -r requirements.txt

```




3. Run the app:


```bash

flask run

```


You may also run the algorithms without the Flask UI. There's a simple driver code `driver_code.py` in module `src.algorithms` that allow you to verify the results on the input map defined in the driver code.

### Unit testing and test coverage

1. Perform unit testing:


```bash

pytest

```



2. Run the test coverage:


```bash

coverage run --branch -m pytest

```



3. Generate test coverage report:


```bash

coverage report -m

```



Report is generated to *htmlcov* directory. 

Configurations are set in file [.coveragerc](https://github.com/roopekole/ohte-harjoitustyo/blob/master/app/.coveragerc).

### Code quality analysis (PyLint)

1. Perform code quality analysis for source code:
```bash

pylint src

```

2. Change configurations by altering