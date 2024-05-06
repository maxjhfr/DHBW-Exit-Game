from flask import Flask, render_template
from flask_sock import Sock
from flask_socketio import SocketIO
import json


app = Flask(__name__)
sock = Sock(app)
socketio = SocketIO(app)

@app.route('/')
def index():
   return render_template('index.html', minecraft = False)

@sock.route('/')
def recieve(ws):

   while True:
      data = ws.receive()
      data = str(data).replace("'", '"')

      try:
         data = json.loads(data)

         if isinstance(data, dict) and 'type' in data:

            if data['type'] == 'minecraft':
               value = data.get('value')
               if value == 'done':
                  print('minecraft done')
                  socketio.emit('minecraft_done', {'data': 4})
               elif value == 'connected':
                  print('minecraft connected')
                  socketio.emit('minecraft_connected')

            if data['type'] == 'nfc_raspi':
               value = data.get('value')
               if value == 'read':
                  socketio.emit('nfc_raspi_read')


         else:
            print('Invalid JSON format: ', data)
      except Exception as e:
         print('Error while processing JSON: ', str(e))


if __name__ == "__main__":
  app.run("0.0.0.0", port=5000)