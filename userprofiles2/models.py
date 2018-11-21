from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


GENDER = (('man', 'Man'), ('woman', 'Woman'))


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, related_name="profile",
                                verbose_name=_('User'), on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(
        null=True, blank=True, verbose_name=_('Phone'))
    gender = models.CharField(
        max_length=40, blank=True, verbose_name=_('Gender'), choices=GENDER)
    avatar = models.ImageField(
        upload_to='userprofiles2/avatars', blank=True, verbose_name=_('Avatar'))
    completion_level = models.PositiveSmallIntegerField(
        default=0, verbose_name=_('Profile completion percentage'))
    email_is_verified = models.BooleanField(
        default=False, verbose_name=_('Email is verified'))
    personal_info_is_completed = models.BooleanField(
        default=False, verbose_name=_('Personal info completed'))

    class Meta:
        verbose_name = _('User profile')
        verbose_name_plural = _('User profiles')

    def __str__(self):
        return "User profile: %s" % self.user.username

    def get_completion_level(self):
        completion_level = 0
        if self.email_is_verified:
            completion_level += 50
        if self.personal_info_is_completed:
            completion_level += 50
        return completion_level

    def update_completion_level(self):
        self.completion_level = self.get_completion_level()
        self.save()
