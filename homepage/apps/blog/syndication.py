from django.conf import settings
from django.contrib.syndication.views import Feed
from markdown import markdown

from .models import Post

class LatestPostsFeed(Feed):
    title = settings.FEED_TITLE
    link = settings.FEED_URL
    description = settings.FEED_TITLE

    def items(self):
        return Post.objects.order_by('-created')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown(item.ingress) + markdown(item.body)