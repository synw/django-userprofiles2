# Django Userprofiles

User profiles management that work with [Django Allauth](https://github.com/pennersr/django-allauth)

To install:

Clone and:

   ```bash
pip install django-allauth django-avatar django-bootstrap3 django-bootstrap-form django-braces
mkdir media/userprofiles
mkdir media/userprofiles/avatars
  ```
  
Installed apps:

   ```python
'django.contrib.sites.models.Site',
'braces',
'allauth',
'allauth.account',
'allauth.socialaccount',
'bootstrap3',
'bootstrapform',
'avatar',
'userprofiles',
  ```
  
Be sure to have ``SITE_ID = 1`` in settings.

Urls:

   ```python
url(r'^avatar/', include('avatar.urls')),
url(r'^account/', include('allauth.urls')),
url(r'^profile/', include('userprofiles.urls')),
  ```
  
Note: you must have Bootstrap and Jquery loaded for the templates to work properly.

Example settings for Allauth:

   ```python
LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = "/account/logout/"

#~ Allauth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
SOCIALACCOUNT_EMAIL_REQUIRED = False
SOCIALACCOUNT_EMAIL_VERIFICATION  = False
ACCOUNT_PASSWORD_MIN_LENGTH = 8
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/account/'
  ```

Note: the templates use bootstrap and font-awesome.