from time import sleep
import json
from channels import Group
from channels.sessions import channel_session ,http_session
from urllib.parse import parse_qs
from django.http import HttpResponse
from channels.handler import AsgiHandler
from django.shortcuts import render
from django.contrib import sessions
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http ,http_session
from django.utils.html import escape
from authentication.models import User
from .models import Chat,Message
# Connected to websocket.connect
chat_rooms = Chat.objects.all()
chat_room_names = chat_rooms.values_list('name',flat=True)
online_users = {k:[] for k in chat_room_names}
repeated_users ={k:[] for k in chat_room_names}
def send_old_messages(chat_name,channel):
    messages = Message.objects.filter(chat=Chat.objects.get(name = chat_name))
    for message in messages:
        channel.send({
            "text": json.dumps({
                "type": "old_messages",
                "text": message.message,
                "username": message.from_user.username,
                "online": len(online_users[chat_name]),
                "usersonline": online_users[chat_name],
             }),
        })
# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message, room_name="dis"):
    # Accept connection
    message.reply_channel.send({"accept": True})
    id = message.http_session['user']
    user = User.objects.get(id=id)
    name = user.username
    # Parse the query string
    # params = parse_qs(message.content["query_string"])
    if name !="" and room_name in chat_room_names:
        # Set the username in the session
        message.channel_session["id"] = id
        message.channel_session["user"] = name
        message.channel_session["room"] = room_name
        # Add the user to the room_name group
        Group("chat-%s" % room_name).add(message.reply_channel)
        if name not in online_users[room_name]:
            online_users[room_name].append(name)
            #sleep(0.1)
            Group("chat-%s" % room_name).send({
                "text": json.dumps({
                    "type": "connected",
                    "text": "connected",
                    "username": escape(message.channel_session["user"]),
                    "online": len(online_users[room_name]),
                    "usersonline": online_users[room_name],
            }),
        })
        else:
            repeated_users[room_name].append(name)
            Group("chat-%s" % room_name).send({
                "text": json.dumps({
                    "type": "reconnected",
                    "username": escape(message.channel_session["user"]),
                    "online": len(online_users[room_name]),
                    "usersonline": online_users[room_name],
            }),
        })
        send_old_messages(room_name,message.reply_channel)
    else:
        # Close the connection.
        message.reply_channel.send({"close": True})
# Connected to websocket.receive
@channel_session_user_from_http
def ws_message(message,room_name="dis"):
    Group("chat-%s" % room_name).send({
        "text": json.dumps({
            "type": 'message',
            "text": escape(message["text"]),
            "username":  escape(message.channel_session["user"]),
            "online": len(online_users[room_name]),
            "usersonline": online_users[room_name],
        }),
    })
    msg =Message()
    msg.chat= Chat.objects.get(name = room_name)
    msg.from_user= User.objects.get(id =message.channel_session["id"])
    msg.message = message["text"]
    msg.private = False
    msg.save()
# Connected to websocket.disconnect
@channel_session_user_from_http
def ws_disconnect(message, room_name="dis"):
    user = message.channel_session["user"]
    if user not in repeated_users[room_name]:
        online_users[room_name].remove(user)
        Group("chat-%s" % room_name).send({
                "text": json.dumps({
                    "type": 'disconnected',
                    "text": "disconnected",
                    "username": escape(user),
                    "online": len(online_users[room_name]),
                    "usersonline": online_users[room_name],
                }),
        })
    else:
        repeated_users[room_name].remove(user)
    Group("chat-%s" % room_name).discard(message.reply_channel)
