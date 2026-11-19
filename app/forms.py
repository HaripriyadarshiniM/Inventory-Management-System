from django import forms
from .models import Product, Supplier

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'sku',
            'supplier',
            'category',
            'price',
            'quantity_in_stock'
        ]
    
    def clean_quantity_in_stock(self):
        quantity = self.cleaned_data.get('quantity_in_stock')
        if quantity < 0:
            raise forms.ValidationError("Quantity in stock cannot be negative.")
        return quantity

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'contact_email',
            'phone_number'
        ]