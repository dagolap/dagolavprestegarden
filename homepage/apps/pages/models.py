from django.db import models
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
    title = models.CharField(_("title"), max_length=75)
    body = models.TextField(_("body"))
    slug = models.CharField(_("slug"), max_length=100)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('page', kwargs={"slug":self.slug})

    def __unicode__(self):
        return self.title