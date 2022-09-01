"""
ASGI config for face_recognition project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
#12, 13 websocket 
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'face_recognition.settings')

application = ProtocolTypeRouter({
    #calls http protocol
  "http": get_asgi_application(),
  #connect browser with the server, syncrhonise. You don't need to refresh
  "websocket": AuthMiddlewareStack(
        URLRouter(
            app.routing.websocket_urlpatterns
        )
    ),
})
