#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

PORT_NUMBER = 80

class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes('Hi {}, Welcome!'.format(self.path.strip('/')), 'utf8'))
        return

def run():
    httpd = HTTPServer(('0.0.0.0', PORT_NUMBER), myHandler)
    httpd.serve_forever()

run()

#commit: add comment
