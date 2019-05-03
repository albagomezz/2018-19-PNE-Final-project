# Alba Gomez de la Flor

import http.server
import termcolor
import socketserver
import requests

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
            contents1 = f.read()
            f.close()

        elif self.path.startswith("/listSpecies"):
            HOSTNAME = "rest.ensembl.org"
            ENDPOINT = "/info/species?"
            r1 = requests.get(HOSTNAME + ENDPOINT, headers = {"Content-Type": "application/json"})
            s1 = r1.json()
            species = s1['species']

            if self.path.startswith("/listSpecies?limit="):
                msg = msg.split("=")


        elif self.path.startswith("/karyotype"):
            fff = open("karyotype.html", "r")
            contents2 = fff.read()
            fff.close()

            if self.path.startswith("/karyotype?specie="):
                HOSTNAME = "rest.ensembl.org"
                ENDPOINT = "/info/species?"
                r2 = requests.get(HOSTNAME + ENDPOINT, headers = {"Content-Type": "application/json"})
                s2 = r2.json()
                species = s2['species']
                for i in species:
                    species2 = [i]







