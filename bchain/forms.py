from django import forms

class DataForm(forms.Form):
    #Used for adding New Record
    amount = forms.CharField(label='Amount',max_length=100)
    location=forms.CharField(label='Location',max_length=100)
    buyer = forms.CharField(label='Buyer', max_length=100)
    seller =forms.CharField(label='Seller',max_length=100)

class NodeForm(forms.Form):
    #Used for inserting new nodes in the system
    url = forms.CharField(label='Node URL',max_length=100)

