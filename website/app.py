from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_socketio import SocketIO, emit

from app_opener import AppOpener


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
app_opener = AppOpener()

#game states to save False is not done, True is done, scan is a rfid scan
game_variables = [
    ("rfid_scanned", False),
    ("rfid_scanned", False),
    ("minecraft_done", False),
    ("rfid_scanned", False),
    ("lamps_done", False),
    ("rfid_scanned", False),
    ("quiz_done", False),
    ("rfid_scanned", False),
    ("sudoku_done", False),
    ("rfid_scanned",False)
]

game_status = 0

@app.route('/')
def redirect_to_hub():
    return redirect(url_for('hub'))

@app.route('/hub', methods=['GET'])
def hub():
    return render_template('main.html')

@app.route('/hub', methods=['POST'])
def get_data():
    global game_status
    data = request.get_json()
    print(data)

    type = data.get('type')
    value = data.get('value')

    required_type = game_variables[game_status][0].split("_")[0]
    required_value = game_variables[game_status][0].split("_")[1]

    # check if the sent POST request is the correct one
    if type != required_type or value != required_value or len(game_variables) < game_status:
        return jsonify({'status': 'failed', 'data_received': data})
    else:
        game_status += 1

    # checks which post request it is
    match data.get("type"):

        case "rfid":
            if data.get("value") == "scanned":
                emit('rfid_scanned', {"game_status": game_status})
                
                # which game to open and what to do
                match game_status:
                    #start sound
                    case 0:
                        game_variables[game_status] = True
                        return jsonify({'status': 'success', 'play_song': game_status})
                    #minecraft game intro
                    case 1:
                        #open minecraft
                        game_variables[game_status] = True
                        app_opener.focus_by_title("Minecraft")
                        return jsonify({'status': 'success', 'play_song': game_status})
                    #lämpchen game intro
                    case 3:
                        game_variables[game_status] = True
                        return jsonify({'status': 'success', 'play_song': game_status})
                    #quiz intro
                    case 5:
                        game_variables[game_status] = True
                        return jsonify({'status': 'success', 'play_song': game_status})
                    #sudoku
                    case 7:
                        game_variables[game_status] = True
                        return jsonify({'status': 'success', 'play_song': game_status})
                    #end sound
                    case 9:
                        game_variables[game_status] = True
                        return jsonify({'status': 'success', 'play_song': game_status})
                    #let rasberry know that there is no sound to play (wrong order of game)
                    case _:
                        return jsonify({'status': 'no_sound'})


        case "minecraft":
            if data.get("value") == "done":
                emit('minecraft_done')

    return jsonify({'status': 'success', 'data_received': data})

@app.route('/sudoku')
def sudoku():
  return render_template('sudoku.html')

@app.route('/quiz')
def quiz():
  return render_template('quiz.html')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, port=5000)
