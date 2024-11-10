from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    success_url = 'success'
    template_name = 'contact_form/contact_form.html'
    name = forms.CharField(required=True)
    email = forms.CharField(validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)