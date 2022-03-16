import requests
import time

ip = ""
pings = 0
interval = 0.0

def bootup():
    print("Ping Machine v1.0")
    time.sleep(1)

def askUser(prompt, error):
    while True:
        try:
            response = input(prompt)
            break
        except ValueError:
            print(error)
    return response

def getPingDestination():
    tempip = askUser("Enter the destination to ping or leave blank for continuous: ", "Input must be a valid IP address")
    
    return(ip)

def getPingAmount():
    pings = 0
    while True:
        try:
            pings = int(input("Enter the amount of pings or leave blank for continuous: "))
            break
        except ValueError:
            print("Input must be a positive integer")
    return pings

def getPingInterval():
    interval = 0.0
    while True:
        try:
            interval = float(input("Enter the interval in seconds or leave blank for continuous: "))
            break
        except ValueError:
            print("Input must be a positive integer")
    return interval

bootup()
ip = getPingDestination()
while ip == "":
    ip = getPingDestination()

pings = getPingAmount()
if pings == "" or pings == 0:
    pings = True
interval = getPingInterval()
n = 0

def ping():
    global n
    while n != pings:
        try:
            response = requests.get(ip)
            n += 1
        except requests.exceptions.ConnectionError:
            print("Ping #" + str(int(n)) + " to '" + ip + "' failed")
        else:
            print("Ping #" + str(int(n)) + " to '" + ip + "' suceeeded with " + str(response.elapsed.total_seconds() * 1000) + "ms of latency")
        if n == pings:
            print("Finished pinging '" + ip + "', now exiting")
            exit()
        else:
            time.sleep(interval)
            ping()
            n += 1

ping()