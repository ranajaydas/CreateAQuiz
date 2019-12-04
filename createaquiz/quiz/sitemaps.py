from django.contrib.sitemaps import GenericSitemap, Sitemap
from .models import Quiz, Tag

tag_sitemap_dict = {
    'queryset': Tag.objects.all(),
}
TagSitemap = GenericSitemap(tag_sitemap_dict)


class QuizSitemap(Sitemap):
    def items(self):
        return Quiz.objects.all()

    def lastmod(self, quiz):
        return quiz.pub_date
