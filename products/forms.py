from django import forms
from products.models import Products

# class Product_form(forms.Form):
#     name = forms.CharField(max_length=40)
#     price = forms.FloatField()
#     description = forms.CharField(max_length=200)
#     SKU = forms.CharField(max_length=30)
#     active = forms.BooleanField()

class Product_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'