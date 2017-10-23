from channels.routing import route
#from chat.consumers import ws_connect, ws_message, ws_disconnect
channel_routing = [
#    route("http.request", "authentication.consumers.http_confirm_email",path=r"^/emailconfirm/(?P<email>[a-zA-Z0-9_@.]+)/(?P<confirmation>[a-zA-Z0-9_]+)/$"),
    route("websocket.connect", "chat.consumers.ws_connect", path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"), 
    route("websocket.receive", "chat.consumers.ws_message", path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    route("websocket.disconnect", "chat.consumers.ws_disconnect", path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
]

