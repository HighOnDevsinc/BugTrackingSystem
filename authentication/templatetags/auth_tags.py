from django import template
from authentication.models import MyUser

register = template.Library()


@register.simple_tag
def user_is_manager(user: MyUser):
    return user.type == 'manager'


@register.simple_tag
def user_is_qa(user: MyUser):
    return user.type == 'qa'


@register.simple_tag
def user_is_developer(user: MyUser):
    return user.type == 'developer'
