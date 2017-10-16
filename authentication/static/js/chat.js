
var chatlist= []
var socket = []
var prevmsg = []
function start(chatname='room_one'){
    if(! chatlist.includes(chatname)){
        chatlist.push(chatname)
        var chatwindow = '\n\
            <section class="windows">\n\
                <h1 class="panel-header">'+chatname+'</h1>\n\
                <div class="panel chat" id="'+chatname+'">\n\
                </div>\n\
                <div class="message">\n\
                 <input type="text" name="message" id="message'+chatname+'" value=""/>\n\
                 <button type="button" id="button'+chatname+'" onclick="send()">Send</button>\n\
                </div>\n\
            </section>\n\
        ';
        document.getElementById("dashboard").innerHTML += chatwindow
        document.getElementById("message"+chatname).addEventListener("keydown", function(event) {
            event.preventDefault();
            if (event.keyCode == 13) {
                document.getElementById("button"+chatname).click();
                document.getElementById("message"+chatname).value=""
            }
        });
        socket.push( new WebSocket("ws://" + window.location.host + "/"+ chatname + "/"));
        socket[chatlist.indexOf(chatname)].onmessage = function(e) {
           var data = JSON.parse(e.data)
           document.getElementById(chatname).innerHTML +='<p> '+ data.username + ': </p> <p>'+ data.text + '</p>';
        }
    }
}
function send(chatname='room_one') {
   var message = document.getElementById("message"+chatname).value
   try{
      socket[chatlist.indexOf(chatname)].send(message)
   }catch(err){
      socket[chatlist.indexOf(chatname)].onopen = function() {
        socket[chatlist.indexOf(chatname)].send(message)
      }
   }
}
