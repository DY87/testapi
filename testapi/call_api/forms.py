from django import forms


class ApiForm(forms.Form):
    url = forms.CharField()
    method = forms.CharField()
