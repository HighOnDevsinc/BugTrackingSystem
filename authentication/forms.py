from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authentication.models import MyUser
from django import forms


class SignInForm(AuthenticationForm):
    email = forms.EmailField(
         label="",
         widget=forms.TextInput(attrs={
             'class': 'form-control',
             'placeholder': 'email'
         })
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    class Meta:
        model = MyUser
        fields = ('email',
                  'password')


class SignUpForm(UserCreationForm):
    name = forms.CharField(
        max_length=24,
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name'
        })
    )
    type = forms.ChoiceField(
        choices=MyUser.TYPE_CHOICES,
        label="",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }),
        help_text='<span class="form-text text-muted"><small>Required. 150 ' +
        'characters or fewer. Letters, digits and @/./+/-/_ only.</small>' +
        '</span>'
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }),
        help_text='<ul class="form-text text-muted small"><li>Your password' +
        'can\'t be too similar to your other personal information.</li><li>' +
        'Your password must contain at least 8 characters.</li><li>Your ' +
        'password can\'t be a commonly used password.</li><li>Your password ' +
        'can\'t be entirely numeric.</li></ul>'
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        }),
        help_text='<span class="form-text text-muted"><small>Enter the same ' +
        'password as before, for verification.</small></span>'
    )

    class Meta:
        model = MyUser
        fields = ('name',
                  'type',
                  'email',
                  'password1',
                  'password2')
