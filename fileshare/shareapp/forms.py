from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(max_length = 50)
    subject = forms.CharField(max_length = 50)
    message = forms.CharField(widget = forms.Textarea, max_length = 200)
