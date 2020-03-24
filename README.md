# Something Python Challenge

Create a simple command-line REST client called `restful.py` able to `GET` and `POST` from [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

## Requirements

1. Written in Python 3 using `requests` library (no framework).
2. Should include `requirements.txt` file for `pip3 install -r requirements.txt` into a `venv` virtual environment.
3. `restful.py` should be an executable Linux script. Usage should be `./restful.py` not `python3 restful.py`.
4. Script should use `argparse` library to process the command-line arguments and options.
5. Error-handling: script should always display the response's HTTP status code. If the response code is not `2XX`, the script should exit with an error message and non-zero exit code, and not perform any additional action.
6. Object-oriented: all functionality after argument parsing should be performed by class methods, rather than in procedural-style functions.

### Command-line Arguments and Options

*  Positional argument `METHOD` a choice of `get` or `post`
*  Positional argument `ENDPOINT` is any URI fragment, i.e., `/posts/1`
*  Option `-o OUTFILE, --output OUTFILE` should write response to a JSON file if `OUTFILE` ends with `.json`, or to a CSV file if `OUTFILE` ends with `.csv`. If `OUTFILE` not provided, the default behavior should be to dump the response JSON to `stdout`.

### Version Control

We use Git for version control. Once the challenge is completed, please push your code to a new repository in your personal GitHub or Bitbucket account, then email us the URL so that we can clone and review your submission.

## Example Usage

Getting help:

```
$ ./restful.py -h
usage: restful.py [-h] [-d DATA] [-o OUTPUT] {get,post} endpoint

positional arguments:
  {get,post}            Request method
  endpoint              Request endpoint URI fragment

optional arguments:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  Data to send with request
  -o OUTPUT, --output OUTPUT
						Output to .json or .csv file (default: dump to stdout)
```

GET all posts and dump to console:

```
$ ./restful.py get /posts
```

GET all posts and dump to JSON file:

```
$ ./restful.py get /posts -o test.json
```

GET all posts and dump to CSV file:

```
$ ./restful.py get /posts -o test.csv
```

GET one post and dump to console:

```
$ ./restful.py get /posts/1
```

POST a new dummy post and dump response to console:

```
$ ./restful.py post /posts --data '{title: "CIELO Rocks!", body: "It really really rocks.", userId: 1}'
```

POST a new dummy post and write response to JSON file:

```
$ ./restful.py post /posts -d '{title: "CIELO Rocks!", body: "It really really rocks.", userId: 1}' -o test.json
```
