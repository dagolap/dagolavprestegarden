from django.db import models
from django.utils.translation import ugettext_lazy as _

from filebrowser.fields import FileBrowseField

class Project(models.Model):
    title = models.CharField(_("title"), max_length=50)
    subtitle = models.CharField(_("subtitle"), max_length=75, null=True)
    description = models.TextField(_("description"))
    image = FileBrowseField(_("image"), directory="images/", extensions=[".jpg",".jpeg",".png",".gif"], blank=True, null=True, max_length=200)
    sort_order = models.SmallIntegerField(_("sort order"))
    slug = models.CharField(_("slug"), max_length=100, null=False, unique=True)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('project_details', kwargs={"slug":self.slug})

    def __unicode__(self):
        return self.title