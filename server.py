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

        if self.path == "/" or self.path == "/main.html":
            f = open("main.html", "r")
            cont = f.read()
            f.close()

        elif self.path.startswith("/listSpecies"):
            HOSTNAME = "rest.ensembl.org"
            ENDPOINT = "/info/species?content-type=application/json"
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

            f2 = open("list_menu.html", "r")
            cont = f2.read()
            f2.close()
            for i in species:
                cont = cont + '<p>' + i['name'] + '<p>'

            if self.path.startswith("/listSpecies?limit="):

                f3 = open("listSpecies.html", "r")
                cont = f3.read()
                f3.close()

                message = self.path.split("=")
                msg = message[1]
                msg = int(msg)
                sp = []
                for i in species:
                    name = i['name']
                    sp.append(name)
                lim = sp[:msg]
                for i in lim:
                    cont = cont + '<p>' + i + '<p>'

        elif self.path.startswith("/karyotype"):
            f4 = open("karyotype_menu.html", "r")
            cont = f4.read()
            f4.close()

            if self.path.startswith("/karyotype?specie="):
                message = self.path.split("=")
                specie = message[1]
                HOSTNAME = "rest.ensembl.org"
                ENDPOINT = "/info/assembly/"
                ENDPOINT2 = "?content-type=application/json"
                METHOD = "GET"

                # Connect to the server
                conn = http.client.HTTPSConnection(HOSTNAME)

                headers = {'User-Agent': 'http-client'}

                # Send the request. No body (None)
                # Use the defined headers
                conn.request(METHOD, ENDPOINT + specie + ENDPOINT2, None, headers)

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
                karyotype = s2['karyotype']
                f5 = open("karyotype.html", "r")
                cont = f5.read()
                f5.close()
                cont = cont + "You have chosen " + specie + ": "
                for i in karyotype:
                    cont = cont + i + " "

        elif self.path.startswith("/chromosomeLength"):
            f6 = open ("chromo_menu.html", "r")
            cont = f6.read()
            f6.close()

            if self.path.startswith('/chromosomeLength?specie='):
                message = self.path.split("&")
                msg = message[0].split("=")
                specie = msg[1]
                msg1 = message[1].split("=")
                chromosome = msg1[1]

                HOSTNAME = "rest.ensembl.org"
                ENDPOINT = "/info/assembly/"
                ENDPOINT2 = "?content-type=application/json"
                METHOD = "GET"

                # Connect to the server
                conn = http.client.HTTPSConnection(HOSTNAME)

                headers = {'User-Agent': 'http-client'}

                # Send the request. No body (None)
                # Use the defined headers
                conn.request(METHOD, ENDPOINT + specie + ENDPOINT2, None, headers)

                # Wait for the server's response
                r3 = conn.getresponse()

                # Print the status
                print()
                print("Response received: ", end='')
                print(r3.status, r3.reason)

                # Read the response's body and close
                # the connection
                text_json = r3.read().decode("utf-8")
                conn.close()

                # Generate the object from the json file
                s3 = json.loads(text_json)
                loaded = s3['top_level_region']
                for i in loaded:
                    if chromosome == i['name']:
                        length = i['length']
                    f7 = open("chromo.html", "r")
                    cont = f7.read()
                    f7.close()
                cont = cont + "Chromosome " + chromosome + " from " + specie + ". Its length is: " + str(length)

        elif self.path.startswith('/geneSeq'):
            f8 = open("seq_menu.html", "r")
            cont = f8.read()
            f8.close()

            if self.path.startswith("/geneSeq?gene="):
                message = self.path.split("=")
                gene = message[1]

                HOSTNAME = "rest.ensembl.org"
                ENDPOINT = "/lookup/symbol/homo_sapiens/"
                ENDPOINT2 = "?content-type=application/json"
                METHOD = "GET"

                # Connect to the server
                conn = http.client.HTTPSConnection(HOSTNAME)

                headers = {'User-Agent': 'http-client'}

                # Send the request. No body (None)
                # Use the defined headers
                conn.request(METHOD, ENDPOINT + gene + ENDPOINT2, None, headers)

                # Wait for the server's response
                r4 = conn.getresponse()

                # Print the status
                print()
                print("Response received: ", end='')
                print(r4.status, r4.reason)

                # Read the response's body and close
                # the connection
                text_json = r4.read().decode("utf-8")
                conn.close()

                # Generate the object from the json file
                s4 = json.loads(text_json)
                info = s4['id']

                HOSTNAME = "rest.ensembl.org"
                ENDPOINT = "/sequence/id/"
                ENDPOINT2 = "?content-type=application/json"
                METHOD = "GET"

                # Connect to the server
                conn = http.client.HTTPSConnection(HOSTNAME)

                headers = {'User-Agent': 'http-client'}

                # Send the request. No body (None)
                # Use the defined headers
                conn.request(METHOD, ENDPOINT + info + ENDPOINT2, None, headers)

                # Wait for the server's response
                r5 = conn.getresponse()

                # Print the status
                print()
                print("Response received: ", end='')
                print(r5.status, r5.reason)

                # Read the response's body and close
                # the connection
                text_json = r5.read().decode("utf-8")
                conn.close()

                # Generate the object from the json file
                s5 = json.loads(text_json)
                data = s5['seq']

                f9 = open("seq.html", "r")
                cont = f9.read()
                f9.close()
                cont = cont + "You have chosen " + gene + " and the sequence is: " + data

        elif self.path.startswith("/geneInfo"):

        elif self.path.startswith("/geneCalc"):

        elif self.path.startswith("/geneList"):

        else:
            f8 = open('error.html', 'r')
            cont = f8.read()
            f8.close()

        self.send_response(200)  # Status line: OK!

        # Define the content-type header:
        self.send_header("Content-Type", "text/html\r\n")

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(cont))

        return

# ------------------------
# Server MAIN program
# ------------------------
# Set the new handler
Handler = TestHandler

# Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # Main loop: Attend the client. Whenever there is a new
    # client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")









