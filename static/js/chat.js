var username = document.getElementById("username").value
var chatlist= []
var socket = []
var prevmsg = []
var prevuser = []
function start(chatname="room one", chat_id="room_one"){
    if(! chatlist.includes(chat_id)){
        chatlist.push(chat_id);
        prevmsg.push("");
        prevuser.push('');
        var chatwindow = '\n\
            <section class="windows">\n\
                <h1 class="panel-header">'+chatname+'</h1>\n\
                <p id="users_online_'+chat_id+'">----</p>\n\
                <div class="panel chat" id="'+chat_id+'">\n\
                </div>\n\
                <div class="message">\n\
                 <input type="text" name="message" id="message_'+chat_id+'" value=""\
onkeyup="if (event.keyCode == 13) { send(\''+chat_id+'\'); return false; }"/>\n\
                 <button type="button" id="button'+chatname+'" onclick="send(\''+chat_id+'\')">Send</button>\n\
                </div>\n\
            </section>\n\
        ';
        document.getElementById("dashboard").innerHTML += chatwindow
        socket.push( new WebSocket("ws://" + window.location.host + "/"+ chat_id + "/"));
        socket[chatlist.indexOf(chat_id)].onmessage = function(e) {
           var data = JSON.parse(e.data);
           if (username == data.username && data.type=="connected"){
              document.getElementById(chat_id).innerHTML += 'welcome';
              document.getElementById("users_online_"+chat_id).innerHTML="users online now: "+data.online+" : "+data.usersonline ;
              document.getElementById(chat_id).scrollTo(0,document.getElementById(chat_id).scrollHeight);
              return;
           }else if(data.type== "reconnected"){
              document.getElementById("users_online_"+chat_id).innerHTML="users online now: "+data.online+" : "+data.usersonline ;
              return;
           }else if(data.username == prevuser[chatlist.indexOf(chat_id)] ){
              document.getElementById(chat_id).innerHTML +='<br>'+ data.text + '';
           }else if(data.username == username){
              document.getElementById(chat_id).innerHTML +='<p>me: </p>'+ data.text + '';
           }else{
              prevmsg[chatlist.indexOf(chat_id)] = '';
              document.getElementById(chat_id).innerHTML +='<p>'+ data.username +':</p>'+ data.text + '';
           }
           prevuser[chatlist.indexOf(chat_id)] = data.username;
           document.getElementById("users_online_"+chat_id).innerHTML="users online now: "+data.online+" : "+data.usersonline ;
           document.getElementById(chat_id).scrollTo(0,document.getElementById(chat_id).scrollHeight);
        }
    }
}
function send(chat_id='room_one') {
   var message = document.getElementById("message_"+chat_id).value;
   document.getElementById("message_"+chat_id).value="";
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
