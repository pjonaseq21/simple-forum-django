"""
ASGI config for blog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
from channels.auth import AuthMiddlewareStack
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket':AuthMiddlewareStack( URLRouter(
      chat.routing.websocket_urlpatterns
    ),
  ),
})

