from os import error
import requests

while True:
    i = 1
    ping = "http://ps171.org/faculty/" + str(i) + "/profile/"
    response = requests.get(ping)
    i += 1
    if response.status_code == 200:
        print("Success " + ping)
    else:
        print("Error " + ping)