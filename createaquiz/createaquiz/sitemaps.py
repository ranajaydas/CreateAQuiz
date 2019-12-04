from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from quiz.sitemaps import TagSitemap, QuizSitemap


class RootSitemap(Sitemap):
    priority = 0.6

    def items(self):
        return [
            'quiz_list',
            'tag_list',
            'login',
            'register',
        ]

    def location(self, url_name):
        return reverse(url_name)


sitemaps_dict = {
    'quiz': QuizSitemap,
    'roots': RootSitemap,
    'tags': TagSitemap,
}
