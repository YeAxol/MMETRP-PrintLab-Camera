from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send

app = Flask(__name__,template_folder='./templates',static_folder='./static')
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, namespace='/socket')

current_state = "default.html"

@app.route('/', methods=['GET','POST'] )
def remote():
    global current_state
    print("state is =", current_state)
    return render_template(current_state)

@app.route('/refresh', methods=['GET','POST'])
def refresh():
    socketio.emit('aaa')
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
    socketio.emit('refresh_page', namespace='/socket')
    socketio.emit('reset')
    if checkbox_values:
        current_state = "combo.html"
        print("COMBO")
    if "1" in checkbox_values:
        socketio.emit('1')
        print("triggered 1")
    if "2" in checkbox_values:
        socketio.emit('2')
        print("triggered 2")
    if "3" in checkbox_values:
        socketio.emit('3')
        print("triggered 3")
    if "4" in checkbox_values:
        socketio.emit('4')
        print("triggered 4")
    if not checkbox_values:
        current_state = "default.html"
        print("DEFAULT")
    socketio.emit('refresh_page')
    return "Form submitted successfully!"

@socketio.on('connect')
def connect():
    emit('load', current_state)

if __name__ == '__main__':
    socketio.run(app)
