from django.forms import ModelForm
from .models import Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('brand', 'title', 'description', 'price', 'image')
    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['brand'].widget.attrs.update({'class' : 'form-control rounded-0'})
        self.fields['title'].widget.attrs.update({'class' : 'form-control rounded-0'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control rounded-0'})
        self.fields['price'].widget.attrs.update({'class' : 'form-control rounded-0'})