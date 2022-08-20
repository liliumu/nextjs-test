from http.server import BaseHTTPRequestHandler
from .test import hello
from .a.b import c
from cowpy import cow


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = cow.Cowacter().milk(f'{c()} {hello()} Hello from Python from a Serverless Function!')
        self.wfile.write(message.encode())
        return
