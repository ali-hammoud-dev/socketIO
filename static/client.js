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

socket_messages.on('from flask',function(msg){
    alert(msg)
});

socket.on('server orginated',function(msg){
    alert(msg);
})