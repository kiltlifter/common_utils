# -*- coding: utf-8 -*-
"""
Module Docstring
"""

import ssl
import os
from urllib.request import HTTPSHandler, build_opener

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class HTTPSession:
    def __init__(self, headers: dict=None, key: str=None, cert: str=None, password: str=None, encoding: str='utf-8'):
        self.headers = headers
        self.key = key
        self.cert = cert
        self.password = password
        self.encoding = encoding

    def _file_handler(self, file_path, mode):
        with open(file_path, mode) as f:
            return f.read()

    def _opener(self):
        if self.cert and os.path.exists(self.cert):
            context = ssl.create_default_context()
            context.load_cert_chain(self.cert, keyfile=self.key, password=self.password)
            opener = build_opener(HTTPSHandler(context=context))
        else:
            opener = build_opener()
        if self.headers:
            opener.addheaders = [(k, v) for k, v in self.headers.items()]
        return opener

    def request(self, url: str, data: object=None):
        opener = self._opener()
        with opener.open(url, data=data.encode(self.encoding) if data else None) as f:
            meta = vars(f)
            return {'meta': meta, 'response': f.read()}
