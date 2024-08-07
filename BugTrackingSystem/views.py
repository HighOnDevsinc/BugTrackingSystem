from django.views.generic import TemplateView
from django.shortcuts import redirect


class HomeView(TemplateView):
    template_name = 'home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('projects')
        return super().dispatch(request, *args, **kwargs)
