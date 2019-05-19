from django.shortcuts import render
from django.views.generic import FormView
from .models import Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def profile(request):
    return render(request, 'portfolio/index.html', {'title': 'Jerry\'s Portfolio'})


# contacts view for the main page with all the portfolios as well as a 'Contact Me' form.
class MainView(FormView):
    template_name = 'portfolio/index.html'
    form_class = ContactForm
    success_url = '/#contact'

    # to populate a dictionary to use as the template context from the model Project
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['project_list'] = Project.objects.all()
        return context

    # check if the form filled at Contact Me is valid. If yes, proceed to send an email
    def form_valid(self, form):
        subject = "{name} contacted you through your Django Portfolio page".format(
            name=form.cleaned_data.get('name')
        )
        message = "Hey there! I am {name}, you can reach me through my email {email} or call me at {mobile}.".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'),
            mobile=form.cleaned_data.get('mobile'))

        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject=subject,
            message=message,
            from_email=form.cleaned_data.get('email'),
            recipient_list=[settings.EMAIL_HOST_USER],  # email to myself
        )
        return super(MainView, self).form_valid(form)
