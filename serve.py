from http.server import HTTPServer, SimpleHTTPRequestHandler

binding = ('localhost', 8000)

SimpleHTTPRequestHandler.extensions_map['.wasm'] = 'application/wasm'

print("open http://%s:%d" % binding)

httpd = HTTPServer(binding, SimpleHTTPRequestHandler)
httpd.serve_forever()
