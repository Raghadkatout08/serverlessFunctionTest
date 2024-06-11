# Serverlss function
## I will create a peice of code 
from http.server import BaseHTTPRequestHandler  # built in class,  I can use it when I need to create/implement server function

class handler(BaseHTTPRequestHandler):
    def do_Get(self):
        self.send_response(200) # send_response -> inhert, related to BaseHTTPRequestHandler, to allow the developer to response
        self.send_header('Content-type', 'text/plain') # send_header -> response the content type of the message itself
        self.end_headers() # end_headers -> the header size is not fixed
        msg = "Welcome from 401 python class"
        self.wfile.write(msg.encode())

        return
    
# we don't have a port! so I can't run this function locally, we don't have a set up config

# push my function on github 