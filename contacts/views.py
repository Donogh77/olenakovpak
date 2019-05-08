from django.shortcuts import render
from django import forms
from .models import Submit_form
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

import json
import urllib
from django.conf import settings

# Create your views here.

class SubmitForm(forms.ModelForm):
    
    class Meta:
        model = Submit_form
        fields = ('your_name', 'your_email', 'message')

def contacts(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''
            
            if result['success']:
                your_subject = form.cleaned_data['your_name'] + ' has sent you a message'
                message = 'A message from ' + form.cleaned_data['your_email'] + ':\n\n' + form.cleaned_data['message']
                your_email = '"' + form.cleaned_data['your_email'] + '"'
                try:
                    send_mail(
                        your_subject,
                        message,
                        your_email,
                        ('donogh@ya.ru',),
                        fail_silently=False,
                    )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return render(request, 'contacts/email_sent.html', {})
            else:
                return render(request, 'contacts/invalid_recaptcha.html', {})
    else:
        form = SubmitForm()
    return render(request, 'contacts/post_list.html', {'form': form})