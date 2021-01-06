from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import userdata, companyData

class signupForm(UserCreationForm):

    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email', 'username'}
        labels = {
            'email' : 'Email',
        }

        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'id' : 'defaultRegisterFormFirstName',
                'placeholder' : 'First name',
            }),
            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'id' : 'defaultRegisterFormLastName',
                'placeholder' : 'Last name',
            }),
            'email' : forms.TextInput(attrs={
                'class' : 'form-control',
                'id' : 'defaultRegisterFormEmail',
                'placeholder' : 'Email',
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'id' : 'defaultRegisterFormUsername',
                'placeholder' : 'Username',
            }),
            'password1' : forms.TextInput(attrs={
                'class' : 'form-control',
                'id' : 'defaultRegisterFormPassword',
                'placeholder' : 'Enter Password',
            }),
            'password2' : forms.TextInput(attrs={
                'class' : 'form-control',
                'id' : 'defaultRegisterFormPassword',
                'placeholder' : 'Confirm password',
            }),
        }

class loginForm(AuthenticationForm):
    
    class Meta:

        widget = {
            'username' : forms.TextInput(attrs={
                'id' : 'defaultLoginFormUsername',
                'class' : 'form-control mb-4',
                'placeholder' : 'Username',
            }),
            'password' : forms.TextInput(attrs={
                'id' : 'defaultLoginFormPassword',
                'class' : 'form-control mb-4',
                'placeholder' : 'Password',
            })
        }

class userdataForm(forms.ModelForm):

    class Meta:
        model = userdata
        exclude = ['studid']
        #fields = "__all__"
        labels = {
            'classis':'Class',
            'tenth_marks': '10th Percentage',
            'twelth_marks': '12th Percentage',
            'degree_marks': 'Average SGPA',
            'live_back': 'Count of live backlogs'
        }
        widgets = {
            'department': forms.Select(attrs={'class':'form-control'}),
            'classis': forms.Select(attrs={'class':'form-control'}),
            'add_info': forms.Textarea(attrs={'class':'form-control'}),
            'tenth_marks': forms.TextInput(attrs={'size':3, 'class' : 'form-control',}),
            'twelth_marks': forms.TextInput(attrs={'size':3, 'class' : 'form-control',}),
            'degree_marks': forms.TextInput(attrs={'size':4, 'class' : 'form-control',}),
            'live_back': forms.TextInput(attrs={'size':1, 'class' : 'form-control',}),
        }

class companyForm(forms.ModelForm):

    class Meta:
        model = companyData
        exclude = ['selected_stud']
        labels = {
            'cname': 'Comapny Name',
            'tenth_marks': '10th Percentage',
            'twelth_marks': '12th Percentage',
            'degree_marks': 'Average SGPA',
            'live_back': 'Count of live backlogs'
        }
        widgets = {
            'cname' : forms.TextInput(attrs={'class' : 'form-control',}),
            'tenth_marks': forms.TextInput(attrs={'size':3, 'class' : 'form-control',}),
            'twelth_marks': forms.TextInput(attrs={'size':3, 'class' : 'form-control',}),
            'degree_marks': forms.TextInput(attrs={'size':4, 'class' : 'form-control',}),
            'live_back': forms.TextInput(attrs={'size':1, 'class' : 'form-control',}),
        }