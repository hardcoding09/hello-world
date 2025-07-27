from django import forms
from .models import Product 

class ProductForm(forms.ModelForm):
    description = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter product description'}))
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price"
        ]
    
    
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "hello" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")
            

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter product description'}))
    price = forms.DecimalField(decimal_places=2, max_digits=10)
    active = forms.BooleanField(required=False)  # Optional field   
