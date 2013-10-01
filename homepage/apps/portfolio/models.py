from django.db import models
from django.utils.translation import ugettext_lazy as _

from filebrowser.fields import FileBrowseField

class Project(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    image = FileBrowseField(_("image"), directory="images/", extensions=[".jpg",".jpeg",".png",".gif"], blank=True, null=True, max_length=200)
    sort_order = models.SmallIntegerField(_("sort order"))