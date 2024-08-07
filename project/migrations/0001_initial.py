# Generated by Django 5.0.7 on 2024-08-02 19:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssuredBy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DevelopedBy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('user_developer', models.ManyToManyField(related_name='user_developer', through='project.DevelopedBy', to=settings.AUTH_USER_MODEL)),
                ('user_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_qa', models.ManyToManyField(related_name='user_qa', through='project.AssuredBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='developedby',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AddField(
            model_name='assuredby',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.AlterUniqueTogether(
            name='developedby',
            unique_together={('project_id', 'developer_id')},
        ),
        migrations.AlterUniqueTogether(
            name='assuredby',
            unique_together={('project_id', 'qa_id')},
        ),
    ]
