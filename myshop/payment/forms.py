from django import forms

class OrderPaymentForm(forms.Form):
    email = forms.EmailField()
    card_number = forms.DecimalField()
    card_date = forms.DateField()
    card_cvc = forms.DecimalField()
    cardholder_name = forms.CharField()
