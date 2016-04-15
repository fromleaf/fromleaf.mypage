from django import forms
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from fromleaf_common.utils import database as db

# TEMP_DATA: 나중에 지워야 함.
USER_EMAIL = 'fromleaf@gmail.com'

class ContactForm(forms.Form):
    name = forms.CharField()
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        email = self.cleaned_data['email']
        user_member_info = db.get_current_member_info(USER_EMAIL)
        
        email_subject = '{} send mail: {}'.format(name, subject)
        
        if subject and message and email:
            try:
                send_mail(email_subject, message, email, [user_member_info.email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('/contactme/thanks/')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
        
        
        