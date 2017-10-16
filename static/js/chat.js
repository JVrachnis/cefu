
var chatlist= []
var socket = []
var prevmsg = []
function start(chatname="room one", chat_id="room_one"){
    if(! chatlist.includes(chat_id)){
        chatlist.push(chat_id)
        prevmsg.push("")
        var chatwindow = '\n\
            <section class="windows">\n\
                <h1 class="panel-header">'+chatname+'</h1>\n\
                <div class="panel chat" id="'+chat_id+'">\n\
                </div>\n\
                <div class="message">\n\
                 <input type="text" name="message" id="message'+chat_id+'" value=""\
onkeyup="if (event.keyCode == 13) { send(\''+chat_id+'\'); return false; }"/>\n\
                 <button type="button" id="button'+chatname+'" onclick="send(\''+chat_id+'\')">Send</button>\n\
                </div>\n\
            </section>\n\
        ';
        document.getElementById("dashboard").innerHTML += chatwindow
        socket.push( new WebSocket("ws://" + window.location.host + "/"+ chat_id + "/"));
        socket[chatlist.indexOf(chat_id)].onmessage = function(e) {
           var data = JSON.parse(e.data);
           document.getElementById(chat_id).innerHTML +='<p> '+  data.username + ': </p> <p>'+  data.text + '</p>';
           document.getElementById(chat_id).scrollTo(0,document.getElementById(chat_id).scrollHeight);
           prevmsg[chatlist.indexOf(chat_id)] = '';
        }
    }
}
function send(chat_id='room_one') {
   var message = document.getElementById("message"+chat_id).value;
   document.getElementById("message"+chat_id).value="";
   if(prevmsg[chatlist.indexOf(chat_id)] != message && isvalid(message)){
      try{
         socket[chatlist.indexOf(chat_id)].send(message);
      }catch(err){
         socket[chatlist.indexOf(chat_id)].onopen = function() {
           socket[chatlist.indexOf(chat_id)].send(message);
         }
      }
      prevmsg[chatlist.indexOf(chat_id)] = message;
   }
}
function isvalid(tempmessage){
   return tempmessage.replace(new RegExp(' ', 'g'), '') != '';
}

