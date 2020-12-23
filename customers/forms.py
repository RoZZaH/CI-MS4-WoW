from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        exclude = ('user',)


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'primary_phone_number': 'Phone Number',
            'primary_postcode': 'Postal Code',
            'primary_town_or_city': 'Town or City',
            'primary_street_address1': 'Street Address 1',
            'primary_street_address2': 'Street Address 2',
            'primary_county': 'County, State or Locality',
        }

        self.fields['primary_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'primary_country': #adds placeholder to all but country field
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *' #if req
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False #remove if placeholder