from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, label='Введите имя:', required=True)
    balance = forms.DecimalField(max_digits=9, decimal_places=2, required=True)
    age = forms.IntegerField()