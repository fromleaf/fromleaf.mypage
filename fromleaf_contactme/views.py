from django.shortcuts import render

from fromleaf_common.utils import database as db
from fromleaf_common.views import FormCommonView
from fromleaf_contactme.forms import ContactForm


class ContactMeView(FormCommonView):
    template_name = 'fromleaf_contactme/contact.html'
    form_class = ContactForm
    success_url = '/contactme/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactMeView, self).form_valid(form)