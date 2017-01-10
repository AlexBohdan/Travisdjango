from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from mail.forms import SendForm


@csrf_exempt
@login_required
def send_message(request):
    if request.POST:
        send_form = SendForm(request.POST)

        if send_form.is_valid():
            form = send_form.save(commit=False)
            send_mail(form.head, form.message, request.user.email,
                      [form.recipient], fail_silently=False)
            form.author = request.user
            form.save()
            messages.success(request, 'Your message send')
            return redirect('/mail/send')
        else:
            messages.error(request, 'Form not valid')
    else:
        send_form = SendForm()

    args = {'form': send_form}
    return render(request, 'message.html', args)
