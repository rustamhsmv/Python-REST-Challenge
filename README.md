## Installation
- Install [Flask](https://github.com/pallets/flask#installing)
- Setup and activate [virtual envirnoment](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/#installing-virtualenv)
- Install [curl](https://curl.haxx.se/download.html) to call server from command line (optional)

## Configuration
If running on development server, set environment flag:
```
$ export FLASK_ENV=development
````

## Running
Check the usage:
```sh
$ python3 server.py -h
```

### A simple example
```sh
$ python3 server.py 9001 people.csv -d
$ curl -H "Content-Type: application/json" http://0.0.0.0:9001/ids/lastname/Robiner
["3", "6", "7"]
```
