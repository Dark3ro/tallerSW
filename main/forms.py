from django import forms

class NoticiaForm(forms.Form):
    nombre = forms.CharField()
