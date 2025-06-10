import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 5500))
DIRECTORY = "html"

os.chdir(DIRECTORY)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Frontend corriendo en http://0.0.0.0:{PORT}")
    httpd.serve_forever()
