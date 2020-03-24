import sys
from builtins import print
import requests
import argparse


class RequestException(Exception):
    """Something went wrong"""
    pass


def list_to_string(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


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
        urlBase = 'https://jsonplaceholder.typicode.com'
        url = urlBase + args.endpoint

        if 'get' == args.method:
            r = requests.get(url)
            print(r.text)
        else:
            payload = list_to_string(args.data)
            print(args.data)
            print(payload)
            r = requests.post(url, data=payload)
        status = r.status_code
        if status == 200:
            print('status:' + str(status))
        else:
            print('status:' + str(status))
            sys.exit(1)

    except TypeError as e:
        print('Error: arguments must be characters')
        parser.print_help()
        sys.exit(1)
    except RequestException:
        print("RequestException: Something went wrong 2")
        parser.print_help()
        sys.exit(1)

