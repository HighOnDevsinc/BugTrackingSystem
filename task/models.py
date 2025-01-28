from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
import os


def validate_image_format(image):
    valid_extensions = ['.png', '.gif']
    ext = os.path.splitext(image.name)[1].lower()

    if ext not in valid_extensions:
        raise ValidationError('Unsupported file extension. Only .png and .gif are allowed.')

    try:
        img = Image.open(image)
        if img.format.lower() not in ['png', 'gif']:
            raise ValidationError('Invalid image format. Only PNG and GIF formats are allowed.')
    except Exception as e:
        raise ValidationError(f'Invalid image: {e}')


class Task(models.Model):
    STATUS_CHOICES_FEATURE = [
        ('new', 'New'),
        ('started', 'Started'),
        ('completed', 'Completed'),
    ]
    STATUS_CHOICES_BUG = [
        ('new', 'New'),
        ('started', 'Started'),
        ('resolved', 'Resolved'),
    ]
    TYPE_CHOICES = [
        ('feature', 'Feature'),
        ('bug', 'Bug'),
    ]

    title = models.CharField(max_length=200, unique=True)
    deadline = models.DateField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.CharField(max_length=10, default='new')
    screenshot = models.ImageField(upload_to='static/media/', validators=[validate_image_format])
    qa_id = models.ForeignKey(
        'authentication.MyUser',
        related_name='qa_id',
        null=True,
        on_delete=models.SET_NULL
    )
    developer_id = models.ForeignKey(
        'authentication.MyUser',
        related_name='developer_id',
        null=True,
        on_delete=models.SET_NULL
    )
    project_id = models.ForeignKey(
        'project.Project',
        related_name='project_id',
        on_delete=models.CASCADE
    )

    # def save(self, *args, **kwargs):
    #     # Ensure the image is valid before saving
    #     validate_image_format(self.screenshot)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title
