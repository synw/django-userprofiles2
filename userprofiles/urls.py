from django.conf.urls import url
from userprofiles.views import ProfileHomeView, ProfileIdentite

urlpatterns = [
    url(r'^$', ProfileHomeView.as_view(), name='profile-home'),
    url(r'^identity/(?P<pk>[0-9]+)/$', ProfileIdentite.as_view(), name='profile-identity-form'),
]