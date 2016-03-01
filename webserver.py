from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello World!</body></html>"
                self.wfile.write(output)
                print output
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hola World!<a href='\hello>Back to Hello</a></body></html>"
                self.wfile.write(output)
                print output
        except IOError:
            self.send_error(404, "file not found: {}".format(self.path))


def main():
    try:
        port = 8080
        server = HTTPServer(('localhost', port), webserverHandler)
        print "webserver running on port {}".format(port)
        server.serve_forever()
    except KeyboardInterrupt:
        print 'webserver interrupted, closing...'
        server.socket.close()


if __name__ == '__main__':
    main()
