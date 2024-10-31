from http.server import BaseHTTPRequestHandler, HTTPServer
import socket


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello-yandex':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello from artem-gon')
        else:
            self.send_response(404)
            self.end_headers()


class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6


def run(server_class=HTTPServerV6, handler_class=MyHandler, port=80):
    server_address = ('::', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
