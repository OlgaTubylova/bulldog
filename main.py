from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                '<h1>Home</h1><br /><a href="/cats">Cats</a>'.encode('utf8'))
        elif self.path == '/cats':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                '<h1>Cats</h1><br /><a href="/">Home</a>'.encode('utf8'))
        elif self.path.startswith('/img'):
            # /img/1.jpg
            self.send_response(200)
            # if doesn't exist, return 404 Not Found
            # if exists, read file and return it

        else:
            self.send_response(404)
            self.end_headers()


server_address = ('0.0.0.0', 8000)
httpd = HTTPServer(server_address, HTTPHandler)
httpd.serve_forever()


# GET / HTTP/1.1
# Content-Length: 35
# Connection: Keep-Alive
# Keep-Alive: timeout=15, max=100

# GET /cats HTTP/1.1
# Content-Length: 35
# Connection: Keep-Alive
# Keep-Alive: timeout=15, max=100
