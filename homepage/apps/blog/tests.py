from datetime import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post

class BlogPostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="fooUser")
        self.post = Post.objects.create(title="foo", created=datetime.now(), author=self.user)

    def test_should_return_correct_unicode_representation(self):
        self.assertEqual(unicode(self.post), "foo", "Should return title as unicode representation")

    def test_should_return_correct_string_representation(self):
        self.assertEquals(str(self.post), "foo", "Should return title as string representation")