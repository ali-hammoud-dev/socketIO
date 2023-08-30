var socket = io.connect('http://' + document.domain + ':' + location.port);
var socket_messages = io('http://' + document.domain + ':' + location.port + '/messages')
var private_socket = io('http://' + document.domain + ':' + location.port + '/private')

// socket.on('connect', function() {
//     socket.send('I am now connected!');

//     socket.emit('custom event', {'name' : 'Anthony'});

//     socket.on('from_flask', function(msg) {
//         alert(msg['extension']);
//     });

//     socket.on('message', function(msg) {
//         alert(msg);
//     });
// });

function sendMessageToServer() {
    var message = document.getElementById('message').value;
    socket_messages.emit('message from user',message);
    document.getElementById('message').value = '';
}

function sendUsername(){
    var uname = document.getElementById('username').value;
    private_socket.emit('username',uname)
}

function sendPrivateMessage(){
    var recipient = document.getElementById('send_to_username').value;
    var message = document.getElementById('private_message').value;
    private_socket.emit('private-message',{'username':recipient , 'message' : message});
}
private_socket.on('new_private_message',function(msg){
    alert(msg)
})


function join_room(){
    var room = document.getElementById('room-to-join').value;
    var username = document.getElementById('user_roomname').value;
    private_socket.emit('join_room',{'room':room,'username':username})
}

private_socket.on('room_message',function(msg){
    alert(msg)
})


function leave_room(){
    var room = document.getElementById('room-to-join').value;
    var username = document.getElementById('user_roomname').value;
    private_socket.emit('leave_the_room',{'room':room,'username':username})
}

// socket_messages.on('from flask',function(msg){
//     alert(msg)
// });

// socket.on('server orginated',function(msg){
//     alert(msg);
// })

