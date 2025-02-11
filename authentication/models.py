from django.contrib.auth.models \
    import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from project.models import Project, DevelopedBy, AssuredBy


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    TYPE_CHOICES = [
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('qa', 'Quality Assurance'),
    ]

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=24)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    developer_project = models.ManyToManyField(
        Project,
        related_name='developer_project',
        through=DevelopedBy
    )
    qa_project = models.ManyToManyField(
        Project,
        related_name='qa_project',
        through=AssuredBy
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',
                       'type']

    def __str__(self):
        return self.name
