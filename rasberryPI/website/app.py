from flask import Flask, render_template, jsonify, request
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

      try:
         data = json.loads(data)

         print (data)
         if isinstance(data, dict) and 'type' in data:
            if data['type'] == 'minecraft':
               value = data.get('value')
               match value:
                  case 'done':
                     print('minecraft done')
                     socketio.emit('minecraft_done', {'data': 4})
                  case 'connected':
                     print('minecraft connected')
                     socketio.emit('minecraft_connected')

         else:
            print('Invalid JSON format: ', data)
      except Exception as e:
         print('Error while processing JSON: ', str(e))


if __name__ == "__main__":
  app.run("127.0.0.1", port=5000)