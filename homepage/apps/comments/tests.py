from datetime import datetime

from django.test import TestCase

from .models import Comment

class CommentTests(TestCase):
    def setUp(self):
        self.created = datetime.now()
        self.comment = Comment.objects.create(title="foo", author="bar", created=self.created)

    def test_should_return_correct_unicode_representation(self):
        self.assertEqual(unicode(self.comment),
                         "foo by bar on {date}".format(date=unicode(self.created)),
                         "Should return title, author and time as unicode representation")

    def test_should_return_correct_string_representation(self):
        self.assertEquals(str(self.comment),
                          "foo by bar on {date}".format(date=unicode(self.created)),
                          "Should return title, author and time as string representation")