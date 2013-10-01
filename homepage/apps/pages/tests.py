from django.test import TestCase

from .models import Page

class PageTests(TestCase):
    def setUp(self):
        self.page = Page.objects.create(title="foo", body="foo", slug="foo")

    def test_should_return_correct_unicode_representation(self):
        self.assertEqual(unicode(self.page), "foo", "Should return title as unicode representation")

    def test_should_return_correct_string_representation(self):
        self.assertEquals(str(self.page), "foo", "Should return title as string representation")