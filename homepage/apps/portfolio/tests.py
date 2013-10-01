from django.test import TestCase

from .models import Project


class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(title="foo", sort_order=1)

    def test_should_return_correct_unicode_representation(self):
        self.assertEqual(unicode(self.project), "foo", "Should return title as unicode representation")

    def test_should_return_correct_string_representation(self):
        self.assertEquals(str(self.project), "foo", "Should return title as string representation")