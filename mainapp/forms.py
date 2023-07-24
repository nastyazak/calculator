from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        # проверка введенных данных
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь {username} не найден')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data

    class Meta:
        model = User
        fields = {'username', 'password'}


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'phone', 'password1', 'password2')


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = {'name_category', 'category_view'}


class TypeWorkForm(ModelForm):
    class Meta:
        model = TypeWork
        fields = {'name_work', 'work_descrip', 'category', 'hours', 'price'}
