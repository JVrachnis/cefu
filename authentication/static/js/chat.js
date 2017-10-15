function start(){
    socket = new WebSocket("ws://" + window.location.host + "/chat/");
    socket.onmessage = function(e) {
        var data = JSON.parse(e.data)
        document.getElementById('room_one').innerHTML +='<p> '+ data.username + ': </p> <p>'+ data.text + '</p>';
    }
}

function send() {
   var message = document.getElementById("message").value
   try{
      socket.send(message)
   }
   catch(err){
      start()
      socket.onopen = function() {
        socket.send(message);
      }
   }
}

