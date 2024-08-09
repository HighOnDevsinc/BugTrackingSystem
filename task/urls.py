from django.urls import path
from .views import (
    TaskListView,
    TaskAddView,
    TaskStatusUpdateView,
    TaskDeleteView,
    TaskEditView
    )

urlpatterns = [
    path(
        '',
        TaskListView.as_view(),
        name='tasks'
        ),

    path(
        'add_task/',
        TaskAddView.as_view(),
        name='add_task'
        ),

    path(
        'delete/<int:pk>/',
        TaskDeleteView.as_view(),
        name='delete_task'
        ),

    path(
        'edit/<int:pk>/',
        TaskEditView.as_view(),
        name='edit_task'
        ),

    path(
        '<int:pk>/status_update/',
        TaskStatusUpdateView.as_view(),
        name='status_update'
        ),
]
