import requests

print("sending request to stop backend server")
try:
    requests.get("http://127.0.0.1:5000/stop_server")
except:
    print("Webserver already stopped")

print("sending request to stop frontend server")
try:
    requests.get("http://127.0.0.1:5001/stop_server")
except:
    print("Webserver already stopped")
