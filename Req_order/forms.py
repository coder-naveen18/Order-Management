from django import forms
from .models import request_order

class Req_order(forms.ModelForm):
    class Meta:
        model = request_order
        fields = [
            'name', 'address', 'phone', 'pincode', 'type', 'items', 'item_name', 'image', 'description'
        ]
        