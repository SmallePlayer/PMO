import socket

def local_ip():
    hostname = socket.gethostname()
    return hostname

host = str(local_ip())
port = "2000"

