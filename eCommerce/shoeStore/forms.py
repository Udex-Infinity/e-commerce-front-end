from django import forms 
from .models import PaymentInfo
class SearchForm(forms.Form):
    search_shoe=forms.CharField(max_length=100, required=False)
class PaymentForm(forms.ModelForm):
    class Meta:
        model=PaymentInfo
        fields="__all__"
        labels={
            'first_name':'First Name',
            'second_name':'Second Name',
            'phone':'Phone Number',
            'address':'Address',
            'card_number':'Card Number',
            'month':'Month',
            'date':'date'
        }
        error_messages={
            'first_name':{
                'required':'Your first name is required',
            }
        }


    