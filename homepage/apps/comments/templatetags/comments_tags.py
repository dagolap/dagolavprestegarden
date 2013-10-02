from argparse import _ActionsContainer
from django import template

from ..models import Comment
from ..forms import CommentForm

register = template.Library()

@register.inclusion_tag('comments/show-comments.html')
def show_comments(target, host_prefix=None):
    if host_prefix:
        target = host_prefix+target

    form = CommentForm()

    return {
        "comments":Comment.objects.filter(target=target),
        "form":form,
    }
