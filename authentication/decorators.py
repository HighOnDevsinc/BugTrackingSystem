from django.core.exceptions import PermissionDenied


def user_is_manager(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.type == 'manager':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return _wrapped_view


def user_is_qa(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.type == 'qa':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return _wrapped_view


def user_is_developer(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.type == 'developer':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return _wrapped_view
