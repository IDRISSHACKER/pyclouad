from cgitb import handler
import http.server
import socketserver

PORT = 3030
address = ("", PORT)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print(f"serveur demaré sur le port {PORT} ")

httpd.serve_forever()
