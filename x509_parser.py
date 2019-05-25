#!/usr/bin/python

import sys, getopt
import ssl
import socket

from x509Parser import x509Parser

#cert = open(sys.argv[1], 'r').read()

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:p:f:d", ["help", "host=", "port=", "file=", "dump"])
    except getopt.GetoptError as err:
        print(err)
        print_help()
        sys.exit(2)

    cert = None
    host = None
    port = None

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-i", "--host"):
            host = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-f", "--file"):
            cert = open(arg, 'r').read()
        elif opt in ("-d", "--dump"):
            input_cert = ""
            line = input("Enter X509 cert: ")
            
            while "-----END CERTIFICATE-----" not in line:
                input_cert += line
                input_cert += "\n"
                line = input()

            input_cert += "-----END CERTIFICATE-----"

            cert = input_cert
        else:
            print_help
            sys.exit(2)

    if (host and port):
        cert = get_certificate(host, port)
    elif (host):
        cert = get_certificate(host)

    print(x509Parser.x509_to_str(cert))

def print_help():
    print("x509_parser.py -i <host> -p <port> -f <input-file> -d")

def get_certificate(host, port=443, timeout=10):
    context = ssl.create_default_context()
    connection = socket.create_connection((host, port))
    sock = context.wrap_socket(connection, server_hostname=host)
    sock.settimeout(timeout)

    try:
        der_cert = sock.getpeercert(True)
    finally:
        sock.close()

    return ssl.DER_cert_to_PEM_cert(der_cert)

if __name__ == "__main__":
    main(sys.argv[1:])