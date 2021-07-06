from http.server import HTTPServer, BaseHTTPRequestHandler

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        pass
        #self.send_response(200)
        #self.send_header("Content-type", "text/xml")
        #self.end_headers()


    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print(post_data) # <-- Print post data
        print("\n")
        #self._set_headers()


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run(addr='127.0.0.1', port=8000)
