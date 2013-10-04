from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name=_("title"))
    ingress = models.TextField(null=True, verbose_name=_("ingress"))
    body = models.TextField(null=True, verbose_name=_("body"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL ,related_name="posts", null=False, verbose_name=_("author"))
    created = models.DateTimeField(null=False, verbose_name=_("created"))
    slug = models.CharField(max_length=100, null=False, unique=True, verbose_name=_("slug"))
    tags = TaggableManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('post_details', kwargs={"slug":self.slug})

    def get_identifier_url(self):
        return self.get_absolute_url()