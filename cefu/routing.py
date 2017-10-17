from channels.routing import route
#from chat.consumers import ws_connect, ws_message, ws_disconnect
channel_routing = [
    route("http.request", "chat.consumers.http_consumer",path=r"^/chat"),
    route("websocket.connect", "chat.consumers.ws_connect", path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"), 
    route("websocket.receive", "chat.consumers.ws_message", path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
    route("websocket.disconnect", "chat.consumers.ws_disconnect", path=r"^/(?P<room_name>[a-zA-Z0-9_]+)/$"),
]

