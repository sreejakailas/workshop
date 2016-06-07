from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from register import views
from register.views import *
from register.models import *
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/$', UserRegistrationView.as_view(), name='login'),
    url(r'^user/success/', TemplateView.as_view(template_name='page.html'),
        name='page'),
    url(r'^chocolate/add/',AddChocolateView.as_view(), name='Add_chocolate'),
    url(r'^chocolate/success/',AddChocolateView.as_view(template_name='sucess.html'), name='bak'),
    url( r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info"),
    url(r'^user/profile/edit/$', UserProfileUpdateView.as_view(), name='user_profile_update'),
]
