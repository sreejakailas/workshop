from django.shortcuts import render
from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from register.forms import *
from django.views.generic.edit import FormView,UpdateView
from django.core.urlresolvers import reverse_lazy
from mysite import *
from django.views.generic import ListView

# Create your views here.
class Home(ListView):
   template_name="index.html"

   def get_queryset(self):
       return Chocolate.objects.all()

class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "register_user.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = 'user/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)

    def anonymous_required(func):
        def as_view(request, *args, **kwargs):
            redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL)
            if request.user.is_authenticated():
                return redirect(redirect_to)
            response = func(request, *args, **kwargs)
            return response
        return as_view

class AddChocolateView(FormView):
    template_name = "Add_chocolate.html"
    form_class = ChocolateAddForm
    success_url = '/register/user/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)