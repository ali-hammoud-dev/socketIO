from flask import Flask,render_template,request
from flask_socketio import SocketIO , send , emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True

socketio = SocketIO(app)

users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/orginate')
def orginate():
    socketio.emit('server orginated','something happened on the server')
    return '<h1>Sent!</h1>'


# @socketio.on('message')
# def receive_message(message):
#     print(message)
#     send('this is a message from flask !!!!!!!')

# @socketio.on('custom event')
# def receive_custom_event(message):
#     print(f"the custom message is {message['name']}")
#     emit('from_flask',{'extension':'This is a custom event from flask.'},json=True)

@socketio.on('message from user',namespace='/messages')
def receive_message_from_user(message):
    print('USER MESSAGE: {} with session id : {}'.format(message,request.sid))
    emit('from flask',message.upper(),broadcast=True)


@socketio.on('username',namespace='/private')
def receive_username(username):
    users.append({username:request.sid})
    print(users)

if __name__ == '__main__':
    socketio.run(app)