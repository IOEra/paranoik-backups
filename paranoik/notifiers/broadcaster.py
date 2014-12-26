"""
Module contains notification broadcaster, which is responsible for spreading
notifications through all notification providers.
"""

from paranoik.notifiers.mail import EmailNotification

PROVIDERS = (
    EmailNotification,
)


class NotificationBroadcaster(object):
    def __init__(self):
        self._providers = PROVIDERS

    def broadcast(self, title, message):
        for provider_cls in self._providers:
            provider = provider_cls(title, message)
            provider.send()