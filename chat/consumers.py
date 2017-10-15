import json
from channels import Group
from channels.sessions import channel_session ,http_session
from urllib.parse import parse_qs
from django.http import HttpResponse
from channels.handler import AsgiHandler
from django.shortcuts import render
from django.contrib import sessions
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http ,http_session
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
    else:
        # Close the connection.
        message.reply_channel.send({"close": True})

# Connected to websocket.receive
@channel_session_user_from_http
def ws_message(message,room_name="dis"):
    Group("chat-%s" % room_name).send({
        "text": json.dumps({
            "text": message["text"],
            "username": message.channel_session["user"],
        }),
    })
# Connected to websocket.disconnect
@channel_session_user_from_http
def ws_disconnect(message, room_name="dis"):
    Group("chat-%s" % room_name).discard(message.reply_channel)
