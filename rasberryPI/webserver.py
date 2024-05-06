import asyncio
import websockets
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


#send nfc read message to flask
async def send_message_to_flask():
  uri = "ws://192.168.178.63:5000"  
  data = {"type": "nfc_raspi", "value": "read"}
  async with websockets.connect(uri) as websocket:
    try:
      await websocket.send(str(data))
      print("Nachricht gesendet:", str(data))
    except websockets.ConnectionClosed:
      print("Connection to websocket server is closed")
    except websockets.WebSocketException as e:
      print(f"WebSocket error: {e}")  
       
reader = SimpleMFRC522()

for _ in range(10):
    try:
        id, text = reader.read()
        
        asyncio.run(send_message_to_flask())
        asyncio.sleep(2)
    except mfrc522.ReaderException as e:
        print(f"NFC reader error: {e}")
        
        

GPIO.cleanup()

	
	
	
	
