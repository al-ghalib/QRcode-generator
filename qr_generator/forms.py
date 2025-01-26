from django import forms

class QRForm(forms.Form):
    qr_title = forms.CharField(
        label='Enter the title of your QR', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title of your QR'})
        )
    url = forms.URLField(
        label='Enter the URL to be embedded in the QR', 
        max_length=200,
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL to be embedded in the QR'})
        )