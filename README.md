# x509-parser
Simple Python (only supports Python3) utility to help parse X509 certificates. This utility will allow the parsing of x509 certificates via:
1. Directly from a web server.
2. From a text file containing the X509 certificate
3. From the command line.

Usage of the tool is as follows:

#### For parsing a X509 certificate from a web server:

To use the default port of 443:
`python x509_parser.py -i <host>` or `python x509_parser.py --host <host>`

To use a custom port:
`python x509_parser.py -i <host> -p <port>` or `python x509_parser.py --host <host> --port <port>`

#### For parsing a x509 certificate from a text file:

`python x509_parser.py -f <filename>` or `python x509_parser.py -file <filename>`

#### For parsing a x509 certificate from the command line:

`python x509_parser.py -d` or `python x509_parser.py --dump`
