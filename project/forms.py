from .models import Project
from django import forms


class ProjectForm(forms.ModelForm):
    title = forms.CharField(
        max_length=20,
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        }),
        help_text='<span class="form-text text-muted"><small>Required. 20 ' +
        'characters or fewer. Needs to be unique.</small></span>'
    )
    description = forms.CharField(
        max_length=200,
        label="",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Description'
        })
    )

    class Meta:
        model = Project
        fields = ('title',
                  'description',)
