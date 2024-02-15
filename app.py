from mmet_camera import app
from flask_socketio import SocketIO

socketio = SocketIO()
socketio.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)