from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    user_manager = models.ForeignKey(
        'authentication.MyUser',
        on_delete=models.CASCADE
        )
    user_developer = models.ManyToManyField(
        'authentication.MyUser',
        related_name='user_developer',
        through='DevelopedBy'
        )
    user_qa = models.ManyToManyField(
        'authentication.MyUser',
        related_name='user_qa',
        through='AssuredBy'
        )

    def __str__(self):
        return self.title


class DevelopedBy(models.Model):
    developer_id = models.ForeignKey(
        'authentication.MyUser',
        on_delete=models.CASCADE
        )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project_id', 'developer_id')

    def __str__(self):
        return f"{self.project_id} - {self.developer_id}"


class AssuredBy(models.Model):
    qa_id = models.ForeignKey(
        'authentication.MyUser',
        on_delete=models.CASCADE
        )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project_id', 'qa_id')

    def __str__(self):
        return f"{self.project_id} - {self.qa_id}"
