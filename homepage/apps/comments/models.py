from django.db import models
from django.utils.translation import ugettext_lazy as _

class Comment(models.Model):
    title = models.CharField(_("title"), max_length=75, null=False, blank=False)
    comment = models.TextField(_("comment"), null=False, blank=False)
    created = models.DateTimeField(_("created"), null=False, blank=False)
    author = models.CharField(_("author"), max_length=75, null=False, blank=False)
    author_email = models.EmailField(_("author email"))
    author_website = models.URLField(_("author website"))

    active = models.BooleanField(_("active"))

    def __unicode__(self):
        return "{title} by {author} on {created}".format(title=self.title, author=self.author, created=str(self.created))