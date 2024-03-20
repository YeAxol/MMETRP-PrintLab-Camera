from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
from time import sleep

app = Flask(__name__,template_folder='./templates',static_folder='./static')
app.config['SECRET_KEY'] = '53eF8STVyjB5l743ueb7oQ0UIM5Gr5JnkOh3yRHBvJbbG2JIVB'
socketio = SocketIO(app, namespace='/socket')

current_state = "default.html"
values = []

@socketio.on('combo')
def set_combo():
    global values
    socketio.emit('reset')
    if "1" in values:
        socketio.emit('1')
    if "2" in values:
        socketio.emit('2')
    if "3" in values:
        socketio.emit('3')
    if "4" in values:
        socketio.emit('4')
    if "5" in values:
        socketio.emit('5')

@app.route('/', methods=['GET','POST'] )
def remote():
    global current_state
    global values
    return render_template(current_state)

@app.route('/control', methods=['GET'])
def control():
    return render_template('control.html')

@app.route('/submit', methods=['POST'])
def submitform():
    checkbox_values = request.form.getlist('checkbox[]')
    print("Checkbox values:", checkbox_values)
    global current_state
    global values
    values = checkbox_values
    socketio.emit('refresh_page')
    if checkbox_values == ['1','2','3','4','5']:
        current_state = "fiveprinters.html"
        socketio.emit('refresh_page')
    elif checkbox_values:
        current_state = "fourprintersorless.html"
        socketio.emit('refresh_page')
    if not checkbox_values:
        current_state = "default.html"
        socketio.emit('refresh_page')
    return "Form submitted successfully!"

@socketio.on('connect')
def connect():
    emit('load', current_state)

if __name__ == '__main__':
    socketio.run(app)
