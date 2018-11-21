from django.apps import AppConfig
from django.urls import reverse_lazy as _


class Userprofiles2Config(AppConfig):
    name = 'userprofiles2'
    verbose_name = _(u'User profiles')

    def ready(self):
        from userprofiles2 import signals
