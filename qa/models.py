from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Question(models.Model):
    """
    Model for the question that users can aks, and the admin can respond to.default=
    """

    # Choised for the catergory
    CATEGORY_CHOISES = (
        ('online_veiligheid', 'Online Veiligheid'),
        ('hoe', 'Hoe kan ik ...?/Hoe werkt ...?'),
        ('anders', 'Anders'),
    )

    # Choises for the background of the question card
    COLOR_CHOISES = (
        ('teal', 'Teal'),
        ('grey lighten-2', 'Grey'),
        ('red lighten-1', 'Red'),
        ('blue', 'Blue'),
    )

    # Main (headline) of the question
    question = models.CharField(max_length=500)
    # More in depth explaination of the question, not required
    explaination = models.TextField()
    # Awnser from the Mod, Admin (not shown on the ask page!)
    awnser = models.TextField(default='Vraag nog niet beantwoord...')
    # Background color for the card
    color = models.CharField(max_length=50, choices=COLOR_CHOISES, default='Grey')
    # Category of the question
    catergory= models.CharField(max_length=50, choices=CATEGORY_CHOISES, default='Anders')
    # Date/Time the question was created on
    created_on = models.DateTimeField(default=timezone.now)
    # If false, question is not showed on the Q&A page
    published = models.BooleanField(default=False)

    def __str__(self):
        '''
        Return a str representaion of the model
            :return str: The question
        '''
        return self.question

    def get_absolute_url(self):
        '''
        Return the absolute_url of the question, using reverse()
            :retturn str: Absolute url
        '''
        return reverse('qa_question_detail', kwargs={'pk': self.pk})

