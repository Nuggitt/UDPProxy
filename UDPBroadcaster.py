from socket import *
from time import sleep
import random
import json

serverName = '255.255.255.255'
serverPort = 10100
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

carSpeedData = {
    "SensorName": "Philip FartSensor",
    "Speed": 0,
}

while True:
    carSpeedData["Speed"] = random.randint(1, 200)
    json_data = json.dumps(carSpeedData)
    clientSocket.sendto(json_data.encode(), (serverName, serverPort))
    sleep(1)
    print("Data sent" + json_data)
print("UDP Broadcaster closed")