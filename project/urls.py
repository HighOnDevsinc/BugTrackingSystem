from django.urls import path, include
from .views import (
    ProjectListView,
    ProjectDeleteView,
    ProjectAddView,
    ProjectEditView,
    ProjectDetailView,
    AddQAView,
    AddDeveloperView,
    RemoveQAView,
    RemoveDeveloperView,
)

urlpatterns = [
    path(
        '',
        ProjectListView.as_view(),
        name='projects'
        ),

    path(
        'delete/<int:pk>/',
        ProjectDeleteView.as_view(),
        name='delete_project'
        ),

    path(
        'edit/<int:pk>/',
        ProjectEditView.as_view(),
        name='edit_project'
        ),

    path(
        'add/',
        ProjectAddView.as_view(),
        name='add_project'
        ),

    path(
        '<int:pk>/',
        ProjectDetailView.as_view(),
        name='detail_project'
        ),

    path(
        '<int:pk>/add_qa/',
        AddQAView.as_view(),
        name='add_qa'
        ),

    path(
        '<int:pk>/add_developer/',
        AddDeveloperView.as_view(),
        name='add_developer'
        ),

    path(
        '<int:project_pk>/remove_qa/<int:qa_pk>/',
        RemoveQAView.as_view(),
        name='remove_qa'
        ),

    path(
        '<int:project_pk>/remove_developer/<int:developer_pk>/',
        RemoveDeveloperView.as_view(),
        name='remove_developer'
        ),

    path(
        '<int:project_pk>/tasks/',
        include('task.urls')
        )
]
