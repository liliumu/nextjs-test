from http.server import BaseHTTPRequestHandler
from datetime import datetime
from .test import hello
from cowpy import cow


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = cow.Cowacter().milk(f'{hello()} Hello from Python from a Serverless Function!')
        self.wfile.write(message.encode())
        return
