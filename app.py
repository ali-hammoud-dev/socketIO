from flask import Flask,render_template,request
from flask_socketio import SocketIO , send , emit,join_room , leave_room,close_room,disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True

socketio = SocketIO(app)

users = {}

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
    print('USER MESSAGE: {} '.format(message))
    emit('from flask',message.upper(),broadcast=True)


@socketio.on('username',namespace='/private')
def receive_username(username):
    users[username] = request.sid
    print('username Added')


@socketio.on('private-message',namespace='/private')
def private_message(payload):
    receipt_session_id = users[payload['username']]
    message = payload['message']

    emit('new_private_message',message,room=receipt_session_id)

@socketio.on('join_room',namespace="/private")
def handle_join_room(payload):
    room = payload['room']
    join_room(room)
    emit('room_message',f'a new user has joined :{payload["username"]}',room=room)

@socketio.on('leave_the_room',namespace="/private")
def handle_leave_room(payload):
    room = payload['room']
    leave_room(room)
    emit('room_message',f'{payload["username"]} has left the room {room}',room=room)


@app.route('/close/<room>')
def close(room):
    close_room(room,namespace='/private')
    return '<h1>Room Closed! </h1>'

@socketio.on('connect',namespace='/private')
def on_connect():
    print('NEW CONNECTION ESTABLISHED!')

@socketio.on('disconnect',namespace="/private")
def on_diconnect():
    print('CONNECTION ENDED!')


@socketio.on('disconnect_me',namespace='/private')
def disconnect_me():
    disconnect()

if __name__ == '__main__':
    socketio.run(app)