"""
1 Launch start_json_server.sh
2 All status codes: print(reply.status_code)
3 Get -> Receive data
4 Post -> Send new data
5 Put -> Replace some data
6 Delete -> Remove data
7 requests.exceptions.Timeout
8 requests.exceptions.ConnectionError
9 requests.exceptions.InvalidURL
"""
import requests

try:
    reply = requests.get("http://localhost:3000", timeout=1)
    if reply.status_code == requests.codes.ok:
        print("ok")
    for k,v in reply.headers.items():
        print(k, ":", v)
    print(reply.text)
except requests.exceptions.Timeout:
    print("Timeout")
except requests.exceptions.ConnectionError:
    print("ConnectionError")
except requests.exceptions.InvalidURL:
    print("InvalidURL")

