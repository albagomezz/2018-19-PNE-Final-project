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

            f2 = open("listSpecies.html", "r")
            contents_species = f2.read()
            f2.close()
            for i in species:
                contents_species = contents_species + '<p>' + i['name'] + '<p>'

            if self.path.startswith("/listSpecies?limit="):
                msg = self.path.split("=")
                number_species = 0
                f3 = open("listSpecies_limit.html", "r")
                contents_limit = f3.read()
                f3.close()

                for i in species:
                    contents_limit = contents_limit + '<p>' + i['name'] + '<p>'
                number_species = number_species + 1

                if str(number_species) == msg[1]:
                    break

        elif self.path.startswith("/karyotype"):
            f4 = open("karyotype_menu.html", "r")
            contents_karyotype = f4.read()
            f4.close()

            if self.path.startswith("/karyotype?specie="):
                msg = self.path.split("=")
                HOSTNAME = "rest.ensembl.org"
                ENDPOINT = "/info/assembly/{}?".format(msg[1])
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
                karyotype = s2['species']
                f5 = open("karyotype.html", "r")
                result_karyotype = f5.read()
                f5.close()

                for i in karyotype:
                    result_karyotype = result_karyotype + i + " "

        elif self.path.startswith("/chromosomeLength"):
            f6 = open ("chromo_menu.html", "r")
            contents_chromo = f6.read()
            f6.close()

            if self.path.startswith('/chromosomeLength?specie='):
                msg = self.path.split("=")
                list1 = []
                for i in msg:
                    list1 = list1 + i.split("&")

                HOSTNAME = "rest.ensembl.org"
                ENDPOINT = "/info/assembly/{}?".format(list1[1])
                METHOD = "GET"

                # Connect to the server
                conn = http.client.HTTPSConnection(HOSTNAME)

                headers = {'User-Agent': 'http-client'}

                # Send the request. No body (None)
                # Use the defined headers
                conn.request(METHOD, ENDPOINT, None, headers)

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
                name = list1[3]
                for i in s3['top_level_region']:
                    if name == i['name']:
                        length = i['length']

                    f7 = open("chromo.html", "r")
                    result_chromo = f7.read()
                    f7.close()

                f5 = open("karyotype.html", "r")
                result_karyotype = f5.read()
                f5.close()
                result_karyotype = result_karyotype + "Chromosome " + name + " from " + list1[1] + " .Its length is: " + str(length)










