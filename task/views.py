from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import Task
from project.models import Project
from .forms import TaskForm, TaskStatusUpdateForm
from django.shortcuts import get_object_or_404


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    form_class = TaskStatusUpdateForm
    template_name = 'detail_project.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user
        if user.type == 'qa':
            return Task.objects.filter(project_id=self.kwargs['project_pk']).distinct()
        elif user.type == 'developer':
            return Task.objects.filter(project_id=self.kwargs['project_pk']).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        return context


class TaskAddView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'add_task.html'

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, id=self.kwargs['project_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.project_id = self.project
        form.instance.qa_id = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('tasks', kwargs={'project_pk': self.project.pk})


class TaskEditView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'edit_task.html'

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, id=self.kwargs['project_pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(qa_id=self.request.user)

    def form_valid(self, form):
        form.instance.project_id = self.project
        form.instance.qa_id = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('tasks', kwargs={'project_pk': self.project.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, id=self.kwargs['project_pk'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.delete()
        return redirect(reverse('tasks', kwargs={'project_pk': self.project.pk}))
    

class TaskStatusUpdateView(UpdateView):
    model = Task
    form_class = TaskStatusUpdateForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, id=self.kwargs['project_pk'])
        self.task = get_object_or_404(Task, id=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        status = request.POST.get('update_option')
        self.task.status = status
        self.task.save()
        return redirect(reverse('tasks', kwargs={'project_pk': self.project.pk}))
