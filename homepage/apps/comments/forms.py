from django import forms
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Comment

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        #self.helper.form_action = reverse("post_comment")
        self.helper.add_input(Submit("submit", "Submit"))

    class Meta:
        model = Comment
        fields = ["title", "comment", "author", "author_email", "author_website", "target"]