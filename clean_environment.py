import requests

print("sending request to stop backend server")
requests.get("http://127.0.0.1:5000/stop_server")
print("sending request to stop frontend server")
requests.get("http://127.0.0.1:5001/stop_server")