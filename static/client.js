var socket = io.connect('http://127.0.0.1:5000');

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
    socket.emit('message from user',message);
    document.getElementById('message').value = '';
}

socket.on('from flask',function(msg){
    alert(msg)
});