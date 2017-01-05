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

    CATEGORY_CHOISES = (
    ('tip', 'Tip'),
    ('trick', 'Trick'),
    ('bescherm', 'Bescherm Jezelf'),
    ('hoe', 'Hoe kan iets?'),
    ('uitleg', 'Uitleg'),
    )

    title = models.CharField(max_length=500)
    body = models.TextField()
    color = models.CharField(max_length=50, choices=COLOR_CHOISES, default='Grey')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOISES, default='Tip')
    tags = models.CharField(max_length=500, default='')
    created_on = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('info_article_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def return_tags(self):
        return self.tags.split(',')


