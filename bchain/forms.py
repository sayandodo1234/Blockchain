from django import forms

class DataForm(forms.Form):
    amount = forms.CharField(label='Amount',max_length=100)
    location=forms.CharField(label='Location',max_length=100)
    buyer = forms.CharField(label='Buyer', max_length=100)
    seller =forms.CharField(label='Seller',max_length=100)