from http.server import HTTPServer,BaseHTTPRequestHandler
content ='''<html><head><title>Laptop specification</title></head><body style="background-colour:blue;"><h1>CONFIGURATION OF LAPTOP</h1><h2>
Laptop Specification:</h2>
<pre>Device name	TMP215-75-G2
Processor	Intel(R) Core(TM) Ultra 5 125H (1.20 GHz)
Installed RAM	16.0 GB (15.5 GB usable)
Device ID	4011A0B2-D17E-453E-99D3-E61AED35ADB7
Product ID	00342-42784-66344-AAOEM
System type	64-bit operating system, x64-based processor
Pen and touch	No pen or touch input is available for this display
</pre></body>
</html>'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
