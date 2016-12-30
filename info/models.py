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

    title = models.CharField(max_length=500)
    body = models.TextField()
    color = models.CharField(max_length=50, choices=COLOR_CHOISES, default='Grey')
    created_on = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('info_articles', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title



