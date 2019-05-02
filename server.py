import http.server
import termcolor
import socketserver

# Server's port
PORT = 8000
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.command, 'yellow')
        termcolor.cprint(self.path, 'red')

        if self.path == '/' or self.path == '/main.html':
            f = open("main.html", "r")
            contents = f.read()
            f.close()


