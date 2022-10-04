"""
ASGI config for tweeter project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from chat import routing
from .consumers import TokenAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tweeter.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websockets": AllowedHostsOriginValidator(
        TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns))
    )
})
