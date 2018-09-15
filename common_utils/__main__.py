# -*- coding: utf-8 -*-
"""
Add utilities to the commandline
"""

from __future__ import print_function

import sys
import argparse
python_maj_version = float(str(sys.version_info.major)+'.'+str(sys.version_info.minor))

if python_maj_version >= 3.6:
    from .encoding import Base64Util
    from .input_output import FileUtil
    from .unit_conversion import UnitConversion
    from .http_client import HTTPSession
else:
    from .http_client27 import HTTPSession
    from .encoding27 import Base64Util
    from .input_output27 import FileUtil
    from .unit_conversion27 import UnitConversion

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


def joiner(value):
    return ' '.join(value)


def handle_base64():
    if args.encode:
        print(Base64Util.base64_encode_str(joiner(args.encode)))
    elif args.decode:
        print(Base64Util.base64_decode_str(joiner(args.decode)))
    else:
        parser.print_usage()


def handle_pickle():
    if args.input and args.filename:
        FileUtil.pickle_obj(str(joiner(args.input)), args.filename)
        print('Object written to {}'.format(args.filename))
    else:
        print('No output file specified.')
        parser.print_usage()


def handle_unpickle():
    if args.filename:
        print(FileUtil.unpickle_obj(args.filename))
    else:
        print('No pickle file specified')
        parser.print_usage()


def handle_conversion():
    binary = False if args.base10 else True
    val = ' '.join(args.value).strip()
    if args.output == 'string':
        print(UnitConversion.bytes_to_str(int(val), binary=binary, precision=5))
    else:
        print(UnitConversion.str_to_bytes(val, binary=binary))


def parse_alt_headers(alt_headers):
    return dict([tuple(map(lambda b: b.strip(), a.split(':') )) for a in alt_headers]) if alt_headers else None


def handle_request():
    headers = parse_alt_headers(args.headers)
    session = HTTPSession(
        headers=headers,
        cert=args.cert,
        key=args.key,
        password=args.password,
    )
    if args.url:
        r = session.request(url=args.url, data=args.data)
        if r:
            print(r['response'])
            print(r['meta'].get('status'))
    else:
        parser.print_usage()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(help='sub-command help.', dest='command')

    encoding_parser = subparser.add_parser('base64', help='base64 encode/decode a string')
    encoding_parser.add_argument('-e', '--encode', type=str, nargs='+', help='Encode string')
    encoding_parser.add_argument('-d', '--decode', type=str, nargs='+', help='Decode string')

    pickle_parser = subparser.add_parser('pickle', help='pickle stdin as python python obj')
    pickle_parser.add_argument('input', type=str, nargs='+', help='String to pickle')
    pickle_parser.add_argument('-f', '--filename', help='Output filename')

    unpickle_parser = subparser.add_parser('unpickle', help='Unpickle a pickle file')
    unpickle_parser.add_argument('filename', type=str, help='Opens and unpickles file specified')

    unit_parser= subparser.add_parser('convert', help='Convert binary or decimal storage types')
    unit_parser.add_argument('value', nargs='+', help='Value to convert')
    unit_parser.add_argument('-b', '--base10', action='store_true', help='Use base10 format (e.g. 1KB = 1000 Bytes)')
    unit_parser.add_argument('-o', '--output', choices=('string', 'bytes'), help='Action to perform')

    request_parser = subparser.add_parser('request', help='Make a http request')
    request_parser.add_argument('-u', '--url', type=str, help='URL to access')
    request_parser.add_argument('-d', '--data', help='Data used in POST request')
    request_parser.add_argument('-c', '--cert', help='PEM certificate file')
    request_parser.add_argument('-k', '--key', help='PEM keyfile')
    request_parser.add_argument('-p', '--password', help='Password to decrypt certificate')
    request_parser.add_argument('-H', '--headers', nargs='+', help='Alternate headers to use. Use curl format, i.e. -H \'Content-Type: application/json\'')

    args = parser.parse_args()

    if args.command == 'pickle':
        handle_pickle()
        exit(0)
    elif args.command == 'unpickle':
        handle_unpickle()
        exit(0)
    elif args.command == 'base64':
        handle_base64()
        exit(0)
    elif args.command == 'convert':
        handle_conversion()
        exit(0)
    elif args.command == 'request':
        handle_request()
        exit(0)
    else:
        parser.print_help()
