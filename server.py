# Alba Gomez de la Flor

import http.server
import termcolor
import socketserver
import json

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
            contents_main = f.read()
            f.close()

        elif self.path.startswith("/listSpecies"):
            HOSTNAME = "rest.ensembl.org"
            ENDPOINT = "/info/species?"
            METHOD = "GET"

            # Connect to the server
            conn = http.client.HTTPSConnection(HOSTNAME)

            headers = {'User-Agent': 'http-client'}

            # Send the request. No body (None)
            # Use the defined headers
            conn.request(METHOD, ENDPOINT , None, headers)

            # Wait for the server's response
            r1 = conn.getresponse()

            # Print the status
            print()
            print("Response received: ", end='')
            print(r1.status, r1.reason)

            # Read the response's body and close
            # the connection
            text_json = r1.read().decode("utf-8")
            conn.close()

            # Generate the object from the json file
            s1 = json.loads(text_json)

            species = s1['species']

            ff = open("listSpecies.html", "r")
            contents_species = ff.read()
            ff.close()
            for i in species:
                contents_species = contents_species + '<p>' + i['name'] + '<p>'

        elif self.path.startswith("/listSpecies?limit="):
            msg = self.path.split("=")


        elif self.path.startswith("/karyotype"):
            fff = open("karyotype.html", "r")
            contents_karyotype = fff.read()
            fff.close()

            if self.path.startswith("/karyotype?specie="):
                HOSTNAME = "rest.ensembl.org"
                ENDPOINT = "/info/species?"
                METHOD = "GET"

                # Connect to the server
                conn = http.client.HTTPSConnection(HOSTNAME)

                headers = {'User-Agent': 'http-client'}

                # Send the request. No body (None)
                # Use the defined headers
                conn.request(METHOD, ENDPOINT, None, headers)

                # Wait for the server's response
                r2 = conn.getresponse()

                # Print the status
                print()
                print("Response received: ", end='')
                print(r2.status, r2.reason)

                # Read the response's body and close
                # the connection
                text_json = r2.read().decode("utf-8")
                conn.close()

                # Generate the object from the json file
                s2 = json.loads(text_json)
                species2 = s2['species']
                for i in species2:
                    contents_karyotype = contents_karyotype + '<p>' + i['name'] + '<p>' #????







