import http.server
import socketserver
import os

# Render define el puerto en una variable de entorno
PORT = int(os.environ.get("PORT", 5500))
DIRECTORY = os.path.join(os.path.dirname(__file__), "html")  # Ruta absoluta al directorio "html"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Sobreescribimos translate_path para que siempre busque en el directorio "html"
        base_path = DIRECTORY
        path = path.lstrip("/")
        return os.path.join(base_path, path)

# Crear servidor
Handler = CustomHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Frontend corriendo en http://0.0.0.0:{PORT}")
    httpd.serve_forever()
