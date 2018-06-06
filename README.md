#### Installation
- Install [Flask](https://github.com/pallets/flask#installing)
- Setup and activate [virtual envirnoment](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/#installing-virtualenv)
- Install [curl](https://curl.haxx.se/download.html) to call server from command line (optional)

#### Configuration
If running on development server, set environment flag:
```
$ export FLASK_ENV=development
````

#### Running
Check the usage:
```sh
$ python3 server.py -h
```

##### A simple example
```sh
$ python3 server.py 9001 people.csv -d
$ curl -H "Content-Type: application/json" http://0.0.0.0:9001/ids/lastname/Robiner
["3", "6", "7"]
```

### Current State
  - This is very lightweight implementation which fully relies on memory to serve requests and persists data in csv file.
  - Unit tests are missing. Unit tests should mock data input and data store (file I/O, right now).

### How to expand this application in the future
  - To scale this for more people data, 
    - Data should be persisted in DB table. Age and Last Name columns should be indexed for faster seeks. Cassandra should serve the purpose. If record deduplication required, table's partition key should be combination of unique columns (or hash of combination). Integer and date columns should be stored as they are instead of in string format. 
    - A cache (LRU or LFU depends on usage) should be tried to avoid I/O in '/ids/lastname/' queries.
    - '/people/age' response should be paged by changing API to '/people/age?offset=N' and return only K at a time.. This will prevent reading all people data into memory.
