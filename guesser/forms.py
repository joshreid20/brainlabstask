from django import forms

class CountryGuesserForm(forms.Form):
    capital = forms.CharField(label="",
                              widget=forms.TextInput(attrs={'class': 'form-control w-100',
                                                            'placeholder': 'Capital'}))
    correct_capital = forms.CharField(label="", widget=forms.TextInput(attrs={'hidden': True}))
    country = forms.CharField(label="", widget=forms.TextInput(attrs={'hidden': True}))
