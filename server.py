import http.server
import termcolor
import socketserver

# Server's port
PORT = 8000
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):

