from http.server import BaseHTTPRequestHandler
from main import welcome_screen

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        welcome_screen()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("Hello from Python!", "utf-8"))
        return