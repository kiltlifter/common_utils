# -*- coding: utf-8 -*-
"""
Add utilities to the commandline
"""

import argparse
from input_output import FileUtil
from encoding import Base64Util


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

    args = parser.parse_args()

    if args.command == 'pickle':
        handle_pickle()
    elif args.command == 'unpickle':
        handle_unpickle()
    elif args.command == 'base64':
        handle_base64()
    else:
        parser.print_help()
