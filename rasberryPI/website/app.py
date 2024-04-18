from flask import Flask, render_template
from flask_sock import Sock
from flask_socketio import SocketIO, emit


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
      if data is None:
         break
      print(data)

      match data:
         case 'minecraft_done':
            socketio.emit("minecraft_done", 'green')
         case 'minecraft_connected':
            socketio.emit('minecraft_connected', 'green')
      

        

if __name__ == "__main__":
  app.run("127.0.0.1", port=5000)