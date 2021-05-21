# Installation manual

_Installation manual follows a process utilizing BASH (e.g. GitBash or other BASH emulator) in Windows_ 

## Local installation

Local machine requires 

- python3.x (with pip and venv)

_In order to run the below commands python3.x need to be configured in the Windows environment variables. This guide assumes that command python is configured as environment variable_

### Installation guide

1. Clone project to a local directory.

```
$ git clone git@github.com:roopekole/tira-labra.git
```

Alternatively, the source code can be downloaded as a zip file from https://github.com/roopekole/tira-labra.

2. Initiate the virtual environment
```
$ python -m venv venv
$ source venv/Scripts/activate
```

3. Install dependencies contained in requirements.txt

```
$ pip install -r requirements.txt
```

7. Run the application (application opens by default in http://localhost:5000)
```
$ flask run
```