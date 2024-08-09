from django import forms
from .models import Task, validate_image_format
from django.db.models.fields import BLANK_CHOICE_DASH


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title'
        }),
        help_text='<span class="form-text text-muted"><small>Required. 200 ' +
        'characters or fewer. Needs to be unique.</small></span>'
    )
    deadline = forms.DateField(
        label="",
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Deadline (YYYY-MM-DD)'
        })
    )
    type = forms.ChoiceField(
        choices=BLANK_CHOICE_DASH + Task.TYPE_CHOICES,

        label="",
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'id_type'
        })
    )
    screenshot = forms.ImageField(
        label="",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control-file'
        }),
        help_text='<span class="form-text text-muted"><small>Only .png and .gif formats are allowed.</small></span>'
    )

    class Meta:
        model = Task
        fields = ('title',
                  'deadline',
                  'type',
                  'screenshot',)

    def clean_screenshot(self):
        screenshot = self.cleaned_data.get('screenshot')
        print('hello', screenshot)
        validate_image_format(screenshot)
        return screenshot


class TaskStatusUpdateForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('started', 'Started'),
        ('completed', 'Completed'),
        ('resolved', 'Resolved'),
    ]

    status = forms.ChoiceField(
        required=False,
        label="",
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Task
        fields = ('status',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance.type == 'feature':
    #         self.fields['status'].choices = Task.STATUS_CHOICES_FEATURE
    #     elif self.instance.type == 'bug':
    #         self.fields['status'].choices = Task.STATUS_CHOICES_BUG
