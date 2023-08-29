from flask import Flask,render_template
from flask_socketio import SocketIO , send , emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def receive_message(message):
    print(message)
    send('this is a message from flask !!!!!!!')

@socketio.on('custom event')
def receive_custom_event(message):
    print(f"the custom message is {message['name']}")
    emit('from_flask','This is a custom event from flask.')


@socketio.on('custom event click')
def receive_custom_event(message):
    print(f"the custom message is {message}")
    emit('from flask',{'extension':'Flask-SocketIO'},json=True)


if __name__ == '__main__':
    socketio.run(app)