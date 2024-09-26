import http.server
import socketserver
import subprocess
import logging

PORT = 5000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/RunJarvis':
            try:
                subprocess.Popen(["python", r"C:\Users\kinda\OneDrive\Desktop\DESTOP ASSISTANT\Ram.py"])
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"project started successfully")
            except Exception as e:
                logging.error(f"Error starting project: {e}")
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"Error starting project")
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
