# -*- coding: utf-8 -*-
"""
Module Docstring
"""

import ssl
import os
# Imports for python 2 and 3 compatibility
try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request, HTTPSHandler, build_opener
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError, HTTPSHandler, build_opener

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class HTTPSession:
    """
    Utitlity that facilitates new http/https requests
    """
    def __init__(self, headers=None, key=None, cert=None, password=None, encoding='utf-8'):
        self.headers = headers
        self.key = key
        self.cert = cert
        self.password = password
        self.encoding = encoding

    def _opener(self):
        """
        Creates an SSL or default urllib opener
        :return: an opener object
        """
        if self.cert and os.path.exists(self.cert):
            context = ssl.create_default_context()
            context.load_cert_chain(self.cert, keyfile=self.key, password=self.password)
            opener = build_opener(HTTPSHandler(context=context))
        else:
            opener = build_opener()
        if self.headers:
            opener.addheaders = [(k, v) for k, v in self.headers.items()]
        return opener

    def request(self, url, data=None):
        """
        Makes a request on behalf of the client
        :param url: Resource to access
        :param data: payload for a POST operation
        :return: request metadata and response in form of a dict
        """
        opener = self._opener()
        resp = opener.open(url, data=data.encode(self.encoding) if data else None)
        meta = vars(resp)
        return {'meta': meta, 'response': resp.read()}
