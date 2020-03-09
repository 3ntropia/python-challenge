import sys
from builtins import print
import requests
import argparse


class RequestException(Exception):
    """Something went wrong"""
    pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='restful', description='Try an endpoint.')
    parser.add_argument('method', type=str,
                        help='Request method', choices=['get', 'post'])
    parser.add_argument('endpoint', type=str,
                        help='Request endpoint URI fragment')

    parser.add_argument('-d', '--data', type=str, nargs='*',
                        help='Data to send with request')

    parser.add_argument('-o', '--outfile', default='stdout', type=str,
                        help='Output to .json or .csv file (default: dump to stdout)')

    args = parser.parse_args()
    print(args)
    try:
        #v1 = ord(args.method)
        #v2 = ord(args.endpoint)
        urlBase = 'https://jsonplaceholder.typicode.com/'

        if 'get' == args.method:
            r = requests.get(urlBase + args.endpoint)
        else:
            payload = args.data[1:-1]
            print(args.data)
            print(payload)
            r = requests.post(urlBase + args.endpoint, data='{title: CIELO Rocks!, body: It really really rocks., userId: 1}')
        status = r.status_code
        if status == 200:
            print('status:' + str(status))
        else:
            print('status:' + str(status))
            sys.exit(1)
        print(r.text)
    except TypeError as e:
        print('Error: arguments must be characters')
        parser.print_help()
        sys.exit(1)
    except RequestException:
        print("RequestException: Something went wrong 2")
        parser.print_help()
        sys.exit(1)

    """ try:
        # https://jsonplaceholder.typicode.com/
        r = requests.get('https://github.com/timeline.json')
        print("URL:" + r.url)
        status = r.status_code
        if status > 200:
            raise Exception("Something went wrong")
        print(r.text)
    except RequestException:
        print("Something went wrong 2") """