from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
from time import sleep

app = Flask(__name__,template_folder='./templates',static_folder='./static')
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, namespace='/socket')

current_state = "default.html"
values = []

@socketio.on('combo')
def set_combo():
    global values
    socketio.emit('reset')
    print('reset')
    if "1" in values:
        socketio.emit('1')
        print("triggered 1")
    if "2" in values:
        socketio.emit('2')
        print("triggered 2")
    if "3" in values:
        socketio.emit('3')
        print("triggered 3")
    if "4" in values:
        socketio.emit('4')
        print("triggered 4")

@app.route('/', methods=['GET','POST'] )
def remote():
    global current_state
    global values
    print("state is =", current_state)
    return render_template(current_state)

@app.route('/refresh', methods=['GET','POST'])
def refresh():
    socketio.emit('refresh_page')
    print("Page refreshed!")
    return "Page refreshed!"

@app.route('/control', methods=['GET'])
def control():
    return render_template('control.html')

@app.route('/submit', methods=['POST'])
def submitform():
    checkbox_values = request.form.getlist('checkbox[]')
    # Process checkbox values
    print("Checkbox values:", checkbox_values)
    global current_state
    global values
    values = checkbox_values
    socketio.emit('refresh_page')
    if checkbox_values:
        current_state = "combo.html"
        socketio.emit('refresh_page')
        print("COMBO")
    if not checkbox_values:
        current_state = "default.html"
        socketio.emit('refresh_page')
        print("DEFAULT")
    return "Form submitted successfully!"

@socketio.on('connect')
def connect():
    emit('load', current_state)

if __name__ == '__main__':
    socketio.run(app)
