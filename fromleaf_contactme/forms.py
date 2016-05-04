from django import forms
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from fromleaf_common.utils import database as db
from fromleaf_common.utils.database import UserData, CompanyData


class ContactForm(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        user_data = UserData(settings.USER_EMAIL)
        name = self.cleaned_data['name']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        email = self.cleaned_data['email']
        
        
        email_subject = '{} send mail: {}'.format(name, subject)
        
        if subject and message and email:
            try:
                send_mail(email_subject, message, email, [user_data.get_member_info().email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('/contactme/thanks/')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
        
        
        