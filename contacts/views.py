from django.shortcuts import render
from django import forms
from .models import Submit_form
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

class SubmitForm(forms.ModelForm):
    
    class Meta:
        model = Submit_form
        fields = ('your_name', 'your_email', 'message')

def contacts(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            your_subject = form.cleaned_data['your_name'] + ' sent you a message'
            message = form.cleaned_data['message']
            your_email = form.cleaned_data['your_email']
            try:
                import sendgrid
                import os
                from sendgrid.helpers.mail import Email, Content, Mail
                
                sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
                from_email = Email(your_email)
                subject = your_subject
                to_email = Email("donogh@ya.ru")
                content = Content("text/plain", message)
                mail = Mail(from_email, subject, to_email, content)
                response = sg.client.mail.send.post(request_body=mail.get())
                '''
                send_mail(
                    your_subject,
                    message,
                    your_email,
                    ('donogh@ya.ru',),
                    fail_silently=False,
                )
                '''
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/home/')
    else:
        form = SubmitForm()
    return render(request, 'contacts/post_list.html', {'form': form})