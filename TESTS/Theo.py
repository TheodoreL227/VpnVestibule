#theo code check out use
import http.server


class SubdomainHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(b'Hello from your subdomain!')


subdomain_server = http.server.HTTPServer(('subdomain.example.com', 8000), SubdomainHandler)

subdomain_server.serve_forever()

os.system('dig subdomain.example.com')

# dan: cool