from django.forms import formsm, ModelFrom
from .models import Question

class QuestionForm(forms.ModelForm):

    def __init(self, *args, **kwargs):
        super(QuestionForm, self).__init(*args, **kwargs)
        self.fields['question'].label = 'Vraag'
        self.fields['explaination'].label = 'Uitleg'
        self.fields['category'].label = 'Categorie'

    class Meta:
        model = Question
        fields = ['question', 'explaination', 'category']
        help_text = {
                'question'      : ('Uw vraag uitgedrukt in een simpele zin.'),
                'explaination'  : ('Verdere uitleg over uw vraag. (Niet verplicht)'),
                'category'      : ('De catergorie die bij uw vraag past.'),
        }
