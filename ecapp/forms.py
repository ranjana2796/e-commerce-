from django import forms


class DetailsForm(forms.Form):
    name=forms.CharField(label='',max_length=50, widget=forms.TextInput(attrs={'class':'form-row col-md-6 mb-3', 'placeholder':'Enter your name here'}))

    age=forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'form-row col-md-6 mb-3', 'placeholder':'Enter your age here'}))

    mobile=forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'form-row col-md-6 mb-3', 'placeholder':'Enter your mobile number here'}))

    city=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-row col-md-6 mb-3', 'placeholder':'Enter your city here'}))
    
    address=forms.CharField(label='',max_length=200,widget=forms.Textarea(attrs={'class':'form-row col-md-6 mb-3', 'placeholder':'Enter your address here'}))