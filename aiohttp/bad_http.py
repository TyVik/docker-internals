#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Set-Cookie", "uid=4089428921631469354; Expires=Wed, 10-Sep-2031 17:55:54 GMT; Path=/\nSet-Cookie: session=123456; Expires=Wed, 10-Sep-2031 17:55:54 GMT; Path=/")
        # self._headers_buffer.append(
        #     ("Set-Cookie: uid=4089428921631469354; Expires=Wed, 10-Sep-2031 17:55:54 GMT; Path=/\rSet-Cookie: session=123456; Expires=Wed, 10-Sep-2031 17:55:54 GMT; Path=/\r\n").encode('latin-1', 'strict'))
        self.end_headers()

    def _html(self, message):
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi!"))


def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
