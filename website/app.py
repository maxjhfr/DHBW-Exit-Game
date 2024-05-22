from audio.audio_player import AudioPlayer
from app_opener import AppOpener
from recognition.handrecognition import recognise

from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_socketio import SocketIO
from time import sleep
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
app_opener = AppOpener()
audio_player = AudioPlayer()

def update_game_variable(game_variables, index, new_value):
    # Convert to list of lists to allow modifications
    game_variables_modifiable = [list(item) for item in game_variables]
    
    # Find the key and update the value
    i = 0
    for item in game_variables_modifiable:
        if i == index:
            item[1] = new_value
            break
        i += 1
    # Convert back to list of tuples
    updated_game_variables = [tuple(item) for item in game_variables_modifiable]
    return updated_game_variables

#game states to save False is not done, True is done, scan is a rfid scan
game_variables = [
    ("game_started", False),
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
    global game_variables
    global game_status

    data = request.get_json()
    print(data)

    type = data.get('type')
    value = data.get('value')

    required_type = str(game_variables[game_status][0]).split("_")[0]
    required_value = str(game_variables[game_status][0]).split("_")[1]

    # check if the sent POST request is the correct one
    if (type != required_type or value != required_value or len(game_variables) < game_status) and (type != "lamps" and len(value) <= 2):
        return jsonify({'status': 'failed', 'data_received': data})
    

    print("game status: ", game_status)
        

    # checks which post request it is
    match data.get("type"):


        case "game":
            if data.get("value") == "started":
                game_status += 1
                game_variables = update_game_variable(game_variables,game_status, True)

        case "rfid":
            if game_variables[0] == False:
                return jsonify({'status': 'success', "value": "notStarted"})

            if data.get("value") == "scanned":
                # which game to open and what to do
                match game_status:
                    #start sound
                    case 1:
                        game_variables = update_game_variable(game_variables,game_status, True)
                        audio_player.play_sound(game_status - 1)
                        game_status += 1
                        return jsonify({'status': 'success'})
                    #minecraft game intro
                    case 2:
                        #open minecraft
                        game_variables = update_game_variable(game_variables,game_status, True)
                        audio_player.play_sound(game_status - 1)
                        app_opener.focus_by_title("Minecraft")
                        game_status += 1
                        return jsonify({'status': 'success'})
                    #lämpchen game intro
                    case 4:
                        game_variables = update_game_variable(game_variables,game_status, True)
                        audio_player.play_sound(game_status - 1)
                        game_status += 1
                        socketio.emit("lamps_start")
                        return jsonify({'status': 'success'})
                    #quiz intro
                    case 6:
                        game_variables = update_game_variable(game_variables,game_status, True)
                        audio_player.play_sound(game_status - 1)
                        socketio.emit('rfid_scanned', {"open": "quiz"})
                        game_status += 1
                        return jsonify({'status': 'success'})
                    #sudoku
                    case 8:
                        game_variables = update_game_variable(game_variables,game_status, True)
                        audio_player.play_sound(game_status - 1)
                        socketio.emit('rfid_scanned', {"open": "sudoku"})
                        game_status += 1
                        return jsonify({'status': 'success'})
                    #end sound
                    case 10:
                        game_variables = update_game_variable(game_variables,game_status, True)
                        audio_player.play_sound(game_status - 1)
                        socketio.emit('rfid_scanned', {"open": "scratch"})
                        game_status += 1
                        return jsonify({'status': 'success'})
                    #let rasberry know that there is no sound to play (wrong order of game)
                    case _:
                        return jsonify({'status': 'no_sound'})


        case "minecraft":
            if data.get("value") == "done":
                game_status += 1
                socketio.emit('minecraft_done')
                sleep(5)
                app_opener.close_by_title("Minecraft")

        case "lamps":
            if data.get("value") == "2":
                game_status += 1
                socketio.emit("lamps_done")
                return jsonify({'status': 'success'})
            else:
                return jsonify({'status': 'failed'})
            

        case "quiz":
            if data.get("value") == "done":
                game_status += 1
                socketio.emit("quiz_done")
                return jsonify({'status': 'success'})
            return jsonify({'status': 'failed'})
        
        case "sudoku":
            if data.get("value") == "done":
                game_status += 1
                socketio.emit("sudoku_done")
                return jsonify({'status': 'success'})
            return jsonify({'status': 'failed'})
           
            
        

    
    return jsonify({'status': 'success', 'data_received': data})

@app.route('/sudoku', methods=['GET'])
def sudoku():
  return render_template('sudoku.html')

@app.route('/sudoku', methods=['POST'])
def get_data_sudoku():
    data = request.get_json()
    print(data)
    
    type = data.get('type')
    value = data.get('value')

    if type != "sudoku" or value != "done":
        return jsonify({'status': 'failed'})
    
    socketio.emit("activate_camera")
    hi = recognise()
    if (hi):
        hub_data = {"type": "sudoku", "value": "done"}
        requests.post('http://localhost:5000/hub', json=hub_data)
        return jsonify({'status': 'success'})





    

@app.route('/quiz')
def quiz():
  return render_template('quiz.html')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, port=5000)
