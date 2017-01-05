from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

class Article(models.Model):
    """
    Description: Model for the aricles that will be posted on the site
    """

    # Colors that the aricle can be (Just styling)
    COLOR_CHOISES = (
    ('teal', 'Teal'),
    ('grey lighten-2', 'Grey'),
    ('red lighten-1', 'Red'),
    ('blue', 'Blue'),
    )

    # Categories that a article can be
    CATEGORY_CHOISES = (
    ('tip', 'Tip'),
    ('trick', 'Trick'),
    ('bescherm', 'Bescherm Jezelf'),
    ('hoe', 'Hoe kan iets?'),
    ('uitleg', 'Uitleg'),
    )

    # Title of the aricle
    title = models.CharField(max_length=500)
    # Body (Text) of the article
    body = models.TextField()
    # Color in wich the article is diplayed on the site, includes the aricle card and navbar
    color = models.CharField(max_length=50, choices=COLOR_CHOISES, default='Grey')
    # The category the article belongs to
    category = models.CharField(max_length=10, choices=CATEGORY_CHOISES, default='Tip')
    # The tags that can be searched to find an article
    tags = models.CharField(max_length=500, default='')
    # The date/time that article was created
    created_on = models.DateTimeField(default=timezone.now)

    # Returns the absolute url of the article
    def get_absolute_url(self):
        return reverse('info_article_detail', kwargs={'pk': self.pk})

    # Returns a string representatios of the article
    def __str__(self):
        return self.title

    # Returns the tags as list
    def return_tags(self):
        return self.tags.split(',')


