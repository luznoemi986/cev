# app.py - Servidor Backend en Python para el Portafolio de Luz
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8000

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar cabeceras de seguridad y caché básica
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

if __name__ == "__main__":
    print(f"🚀 Servidor de desarrollo corriendo en http://localhost:{PORT}")
    print("📁 Sirviendo archivos estáticos desde la carpeta del proyecto.")
    print("Presiona Ctrl + C para detener el servidor.")
    
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, CustomHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido con éxito.")
