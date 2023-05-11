from .models import OrderComment, Profile, Order
from django import forms
from django.contrib.auth.models import User


class OrderCommentForm(forms.ModelForm):
    class Meta:
        model = OrderComment
        fields = ['content']
        # widgets = {'order': forms.HiddenInput(), 'user': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']


class DateInput(forms.DateInput):
    input_type = 'date'


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['vehicle', 'deadline', 'status']
        widgets = {'owner': forms.HiddenInput(), 'deadline': DateInput()}