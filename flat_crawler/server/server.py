from http import server
from socketserver import TCPServer
import time
#
class MyRequestHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'Flat_page.html'
        return server.SimpleHTTPRequestHandler.do_GET(self)


Handler = MyRequestHandler
wpage=TCPServer(("0.0.0.0", 8080), Handler)


wpage.serve_forever()


#   try:
#       webServer.serve_forever()
#   except KeyboardInterrupt:
#       pass
#
#   webServer.server_close()
#   print("Server stopped.")
