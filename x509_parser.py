#!/usr/bin/python

import sys
import ssl
import socket

from x509Parser import x509Parser

#cert = open(sys.argv[1], 'r').read()

def get_certificate(host, port=443, timeout=10):
    context = ssl.create_default_context()
    conn = socket.create_connection((host, port))
    sock = context.wrap_socket(conn, server_hostname=host)
    sock.settimeout(timeout)
    try:
        der_cert = sock.getpeercert(True)
    finally:
        sock.close()
    return ssl.DER_cert_to_PEM_cert(der_cert)

cert = get_certificate('www.google.com')

x509Parser.parse_x509(cert)