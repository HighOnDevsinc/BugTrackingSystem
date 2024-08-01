from django.urls import path
from .views import HomeView, SignInView, SignUpView, SignOutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_out/', SignOutView.as_view(), name='sign_out'),
]
