
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class DevOpsHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "application": "Python DevOps CI/CD",
                "timestamp": datetime.now().isoformat()
            }
            self.send_response(200)

        elif self.path == "/":
            response = {
                "message": "Welcome to my DevOps project!",
                "version": "1.0.0"
            }
            self.send_response(200)

        else:
            response = {"error": "Not found"}
            self.send_response(404)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), DevOpsHandler)
    print("Application running on port 8000")
    server.serve_forever()
