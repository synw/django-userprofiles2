# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from allauth.account.utils import send_email_confirmation
from braces.views import LoginRequiredMixin
from userprofiles.models import UserProfile
from userprofiles.forms import IdentiteForm, EmailForm


class ProfileHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofiles/home.html'
    user_check_failure_path = '/comptes/signup/'
    
    def check_user(self, user):
        if user.is_active:
            return True
        return False
    
    def get_context_data(self, **kwargs):
        context = super(ProfileHomeView, self).get_context_data(**kwargs)
        profile = UserProfile.objects.get_or_create(user=self.request.user)[0]
        context['profile'] = profile
        return context

    
class ProfileIdentite(LoginRequiredMixin, UpdateView):  
    template_name = "userprofiles/identity_form.html"
    form_class = IdentiteForm
    user_check_failure_path = '/comptes/login/'
    success_url = reverse_lazy("profile-home")
    
    def get_queryset(self):
        queryset = UserProfile.objects.filter(user=self.request.user)
        return queryset
    
    def form_valid(self, form, **kwargs):
        profile = form.save(commit=False)
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        profile.gender = form.cleaned_data['gender']
        profile.phone = form.cleaned_data['phone']
        profile.personal_info_is_completed = True
        profile.completion_level = profile.get_completion_level()
        profile.save()
        #return super(ProfileIdentite, self).form_valid(form)
        return HttpResponseRedirect(self.get_success_url())



    
    
