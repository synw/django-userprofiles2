# Django Userprofiles

User profiles management that work with [Django Allauth](https://github.com/pennersr/django-allauth)

To install:

   ```bash
pip install django-allauth django-avatar django-bootstrap3 django-bootstrap-form
git install git+https://github.com/synw/django-userprofiles.git
mkdir media/userprofiles
mkdir media/userprofiles/avatars
  ```
  
Installed apps:

   ```python
'allauth',
'allauth.account',
'allauth.socialaccount',
'avatar',
'userprofiles',
  ```

Urls:

   ```python
url(r'^avatar/', include('avatar.urls')),
url(r'^profile/', include('userprofiles.urls')),
  ```

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