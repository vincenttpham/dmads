from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import re

# Create your views here.


def wdowinsurance(request):
    return render(request, "wdowinsurance.html")


def get_started(request):
    if request.method == "POST":
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if (len(request.POST['first_name']) < 1) or (len(request.POST['last_name']) < 1) or (len(request.POST['email']) < 1) or (len(request.POST['phone_number']) < 1):
            errors["blank"] = "Please fill all required fields."
        if not EMAIL_REGEX.match(request.POST['email']):
            errors['email'] = "Please enter your email address in format: yourname@example.com"
        if len(errors) > 0:
            for key, value in errors.items():
                messages.warning(request, value, extra_tags=key)
                return redirect('/wdowinsurance')
        try:
            send_mail(
                request.POST['first_name'] + ' ' + request.POST['last_name'],
                request.POST['email'] + ' ' + request.POST['phone_number'] + ' ' + request.POST['occupation'],
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except BadHeaderError:
                return HttpResponse('Invalid header found.')
        messages.info(request, "Your info has been received.")
    else:
        messages.info(request, "Sorry, an internal error has occured. Please refresh the page and try again.")
        return redirect('/wdowinsurance')
    return redirect('https://agents.farmers.com/ca/huntington-beach/aaron-wdowin')