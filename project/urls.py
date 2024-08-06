from django.urls import path # noqa
from .views import \
    ProjectListView, \
    ProjectDeleteView, \
    ProjectAddView, \
    ProjectEditView, \
    ProjectDetailView, \
    AddQAView, \
    AddDeveloperView, \
    RemoveQAView, \
    RemoveDeveloperView

urlpatterns = [
    path(
        'projects/',
        ProjectListView.as_view(),
        name='projects'
        ),

    path(
        'projects/delete/<int:pk>/',
        ProjectDeleteView.as_view(),
        name='delete_project'
        ),

    path(
        'projects/edit/<int:pk>/',
        ProjectEditView.as_view(),
        name='edit_project'
        ),

    path(
        'projects/add/',
        ProjectAddView.as_view(),
        name='add_project'
        ),

    path(
        'projects/<int:pk>/',
        ProjectDetailView.as_view(),
        name='detail_project'),

    path(
        'project/<int:pk>/add_qa/',
        AddQAView.as_view(),
        name='add_qa'),

    path(
        'project/<int:pk>/add_developer/',
        AddDeveloperView.as_view(),
        name='add_developer'),

    path(
        'project/<int:project_pk>/remove_qa/<int:qa_pk>/',
        RemoveQAView.as_view(),
        name='remove_qa'),

    path(
        'project/<int:project_pk>/remove_developer/<int:developer_pk>/',
        RemoveDeveloperView.as_view(),
        name='remove_developer'),
]
