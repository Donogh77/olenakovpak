from django.shortcuts import render
from django import forms
from .models import Submit_form
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.

class SubmitForm(forms.ModelForm):
    
    class Meta:
        model = Submit_form
        fields = ('your_name', 'your_email', 'message')

def contacts(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid:
            form.save()
            subject = form.cleaned_data['your_name'] + ' sent you a message'
            send_mail(
                subject,
                form.cleaned_data['message'],
                form.cleaned_data['your_email'],
                ['donogh@ya.ru',],
                fail_silently=False,
            )
            return HttpResponseRedirect('/home/')
    else:
        form = SubmitForm()
    return render(request, 'contacts/post_list.html', {'form': form})