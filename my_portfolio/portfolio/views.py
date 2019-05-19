from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def profile(request):
    return render(request, 'portfolio/index.html', {'title': 'Jerry\'s Portfolio'})


class MainView(ListView, FormView):
    model = Project
    context_object_name = 'projects'
    template_name = 'portfolio/index.html'
    form_class = ContactForm
    success_url = '/#contact'

    # to populate a dictionary to use as the template context from the model Project
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Project'
        return data

    # check if the form filled at Contact Me is valid. If yes, proceed to send an email
    def form_valid(self, form):
        message = "NAME -- {name}\nEMAIL -- {email}\nMOBILE -- {mobile}\n ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'),
            mobile=form.cleaned_data.get('mobile'))

        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject='Someone contacted you through your Django Portfolio',
            message=message,
            from_email=form.cleaned_data.get('email'),
            recipient_list=[settings.EMAIL_HOST_USER],      # email to myself
        )
        return super(MainView, self).form_valid(form)