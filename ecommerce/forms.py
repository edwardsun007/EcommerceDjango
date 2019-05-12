from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
# django forms gives you a way to
# create your form field which
# provides validation and html handling


class ContactForm(forms.Form):
    # this is Django forms' DOM manipulation here:
    # run this and you see that class and id are added to the input field
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "form_firstname",
                   "placeholder": "Your First Name"}
        ))
    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "id": "form_lastname",
                   "placeholder": "Your Last Name"}
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control",
                   "placeholder": "Email Address"}
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Your message"}
        )
    )

    # customized validation error
    def clean_email(self):
        print('clean_email starts')
        print('clean_email print is_valid()')
        print(self.is_valid())  # this works
        print('clean_email print cleaned_data')
        print(self.cleaned_data)
        email = self.cleaned_data.get("email")  # original input value
        print(email)
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be Gmail!")
        return email


'''
LoginForm
'''


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Your username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Your password"}
        )
    )


'''
RegisterForm
'''


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Your username"}
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Email Address"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Your password"}
        )
    )

    password2 = forms.CharField(
        label='Confirm password',
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Confirm your password"}
        )
    )

    def clean_username(self)

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords must match.")

        return data
