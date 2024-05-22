import requests
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time


def send_message(type, value):
    url = 'http://192.168.178.63:5000'
    data = {'type': type, 'value': value}

    response = requests.post(url, json=data)
    return response

class RFID():
    def __init__(self):
        GPIO.setwarnings(False)

    def readRFID(self):
        reader = SimpleMFRC522()

        try:
            reader.read()
            response = send_message("rfid", "scanned").json()
            print("rread rfid tag.... sending message to flask")
            print("sent")
            GPIO.cleanup()
            return response
        except Exception as e:
            print(f"Read Error: {e}")
        GPIO.cleanup

rfid = RFID()
while True:
    response = rfid.readRFID()
    print(response)
    time.sleep(5)




