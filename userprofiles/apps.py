from django.apps import AppConfig
from django.core.urlresolvers import reverse_lazy as _


class UserProfilesConfig(AppConfig):
    name = 'userprofiles'
    verbose_name = _(u'User profiles')

    def ready(self):
        from userprofiles import signals