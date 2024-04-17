from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('change_button_color')
def change_button_color(data):
    # Process the message from the client (Java)
    if data == 'green':
        # Broadcast message to all connected clients (including website)
        emit('update_button_color', {'color': 'green'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, port = 8765)
