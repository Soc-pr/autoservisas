from .models import OrderComment
from django import forms

class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = OrderComment
        fields = ['content']
        # widgets = {'order': forms.HiddenInput(), 'user': forms.HiddenInput()}
