from django.forms import ModelForm, Form
from django import forms
from .models import Question

class AddQuestion(Form):
    '''
    Class to create the form for the adding of new questions.
    '''

    # Possible choices for the category
    CATEGORY_CHOISES = (
        ('online_veiligheid', 'Online Veiligheid'),
        ('hoe', 'Hoe kan ik ...?/Hoe werkt ...?'),
        ('anders', 'Anders'),
    )

    # Declaration of the question field
    question_field = forms.CharField(
        max_length=500,
        label='Vraag:',
        help_text="Uw vraag in een zin sammengevat.",
        )

    # Decleration of the explaination field
    explaination_field = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),
        label='Uitleg:',
        help_text='Een korte uitleg over uw vraag.',
        )

    # Decelartion of the caterogry field
    catergory_field = forms.ChoiceField(
        choices=CATEGORY_CHOISES,
        widget=forms.Select(attrs={'class': 'browser-default', 'style': 'margin-bottom: 50px;'}),
        label='Categorie:',
        help_text='Kies een passende categorie voor uw vraag.',
        )


