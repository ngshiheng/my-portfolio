from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    mobile = forms.IntegerField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)