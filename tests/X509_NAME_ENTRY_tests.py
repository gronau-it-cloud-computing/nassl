#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from nassl import _nassl
import socket
from nassl.ssl_client import SslClient, OpenSslVerifyEnum


class X509_NAME_ENTRY_Tests(unittest.TestCase):

    def test_new_bad(self):
        self.assertRaises(NotImplementedError, _nassl.X509_NAME_ENTRY, (None))


class X509_NAME_ENTRY_Tests_Online(unittest.TestCase):

    def test(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect(('www.google.com', 443))

        ssl_client = SslClient(sock=sock, ssl_verify=OpenSslVerifyEnum.NONE)
        ssl_client.do_handshake()
        name_entry = ssl_client.get_peer_certificate().get_subject_name_entries()[0];

        self.assertIsNotNone(name_entry.get_data())
        self.assertIsNotNone(name_entry.get_object())


def main():
    unittest.main()

if __name__ == '__main__':
    main()