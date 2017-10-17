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
# Connected to websocket.connect
rooms= {}
repeatedusers={}
def http_consumer(message):

    # Make standard HTTP response - access ASGI path attribute directly
    response = render(message,"main.html")
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message, room_name="dis"):
    # Accept connection
    message.reply_channel.send({"accept": True})
    name = message.http_session['user']
    # Parse the query string
    # params = parse_qs(message.content["query_string"])
    if name !="":
        # Set the username in the session
        message.channel_session["user"] = name
        message.channel_session["room"] = room_name
        # Add the user to the room_name group
        Group("chat-%s" % room_name).add(message.reply_channel)
        if room_name not in rooms:
            rooms[room_name] = []
        if room_name not in repeatedusers:
            repeatedusers[room_name] =[]
        if name not in rooms[room_name]:
            rooms[room_name].append(name)
            #sleep(0.1)
            Group("chat-%s" % room_name).send({
                "text": json.dumps({
                    "type": "connected",
                    "text": "connected",
                    "username": escape(message.channel_session["user"]),
                    "online": len(rooms[room_name]),
                    "usersonline": rooms[room_name],
            }),
        })
        else:
            repeatedusers[room_name].append(name)
            Group("chat-%s" % room_name).send({
                "text": json.dumps({
                    "type": "reconnected",
                    "username": escape(message.channel_session["user"]),
                    "online": len(rooms[room_name]),
                    "usersonline": rooms[room_name],
            }),
        })
    else:
        # Close the connection.
        message.reply_channel.send({"close": True})
# Connected to websocket.receive
@channel_session_user_from_http
def ws_message(message,room_name="dis"):
    msq = message["text"]
    Group("chat-%s" % room_name).send({
        "text": json.dumps({
            "type": 'message',
            "text": escape(message["text"]),
            "username":  escape(message.channel_session["user"]),
            "online": len(rooms[room_name]),
            "usersonline": rooms[room_name],
        }),
    })
# Connected to websocket.disconnect
@channel_session_user_from_http
def ws_disconnect(message, room_name="dis"):
    user = message.channel_session["user"]
    if user not in repeatedusers[room_name]:
        rooms[room_name].remove(user)
        Group("chat-%s" % room_name).send({
                "text": json.dumps({
                    "type": 'disconnected',
                    "text": "disconnected",
                    "username": escape(user),
                    "online": len(rooms[room_name]),
                    "usersonline": rooms[room_name],
                }),
        })
    else:
        repeatedusers[room_name].remove(user)
    Group("chat-%s" % room_name).discard(message.reply_channel)