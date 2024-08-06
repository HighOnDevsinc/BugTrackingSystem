from django.shortcuts import render # noqa
from django.views.generic import ListView, \
    DeleteView, \
    CreateView, \
    UpdateView, \
    DetailView, \
    View
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Project, AssuredBy, DevelopedBy
from authentication.models import MyUser
from .forms import ProjectForm


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'projects'

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(user_manager=user).distinct() | \
            Project.objects.filter(user_developer=user).distinct() | \
            Project.objects.filter(user_qa=user).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = context['projects']
        project_info = []

        for project in projects:
            qa_count = AssuredBy.objects. \
                filter(project_id=project.id). \
                count()
            dev_count = DevelopedBy.objects. \
                filter(project_id=project.id). \
                count()
            project_info.append({
                'project': project,
                'qa_count': qa_count,
                'developer_count': dev_count,
            })

        context['project_info'] = project_info
        return context


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('projects')

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        project.delete()
        return redirect(self.success_url)


class ProjectEditView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'edit_project.html'
    success_url = reverse_lazy('projects')

    def get_queryset(self):
        return self.model.objects.filter(user_manager=self.request.user)

    def form_valid(self, form):
        form.instance.user_manager = self.request.user
        return super().form_valid(form)


class ProjectAddView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'add_project.html'
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.user_manager = self.request.user
        return super().form_valid(form)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'detail_project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()

        assigned_qas = AssuredBy.objects. \
            filter(project_id=project). \
            values_list('qa_id', flat=True)
        qa_users = MyUser.objects. \
            filter(type='qa'). \
            exclude(id__in=assigned_qas)

        assigned_devs = DevelopedBy.objects. \
            filter(project_id=project). \
            values_list('developer_id', flat=True)
        dev_users = MyUser.objects. \
            filter(type='developer'). \
            exclude(id__in=assigned_devs)

        context['qa'] = qa_users
        context['developer'] = dev_users
        context['assured_by'] = AssuredBy.objects. \
            filter(project_id=project)
        context['developed_by'] = DevelopedBy.objects. \
            filter(project_id=project)
        return context


class AddQAView(LoginRequiredMixin, View):
    def post(self, request, pk):
        project = Project.objects.get(pk=pk)
        print(project)
        qa_user_id = request.POST.get('qa')
        qa_user = MyUser.objects.get(pk=qa_user_id)
        AssuredBy.objects.create(project_id=project, qa_id=qa_user)
        return redirect('detail_project', pk=pk)


class AddDeveloperView(LoginRequiredMixin, View):
    def post(self, request, pk):
        project = Project.objects.get(pk=pk)
        dev_user_id = request.POST.get('developer')
        print(dev_user_id)
        dev_user = MyUser.objects.get(pk=dev_user_id)
        DevelopedBy.objects.create(project_id=project, developer_id=dev_user)
        return redirect('detail_project', pk=pk)


class RemoveQAView(LoginRequiredMixin, View):
    def post(self, request, project_pk, qa_pk):
        AssuredBy.objects.filter(
            project_id=project_pk,
            qa_id=qa_pk
            ).delete()
        return redirect('detail_project', pk=project_pk)


class RemoveDeveloperView(LoginRequiredMixin, View):
    def post(self, request, project_pk, developer_pk):
        DevelopedBy.objects.filter(
            project_id=project_pk,
            developer_id=developer_pk
            ).delete()
        return redirect('detail_project', pk=project_pk)
