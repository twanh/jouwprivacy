from django.forms import ModelForm
from .models import Question

class QuestionForm(ModelForm):

    def __init(self, *args, **kwargs):
        super(QuestionForm, self).__init(*args, **kwargs)
        self.fields['question'].label = 'Vraag'
        self.fields['explaination'].label = 'Uitleg'
        self.fields['catergory'].label = 'Categorie'

        # Again, iterate over all of our field objects.
        for field in self._meta.fields:
            # Create a string, get_FIELDNAME_help text
            method_name = "get_{0}_help_text".format(field.name)

            # We can use curry to create the method with a pre-defined argument
            curried_method = curry(self._get_help_text, field_name=field.name)

            # And we add this method to the instance of the class.
            setattr(self, method_name, curried_method)

    def _get_help_text(self, field_name):
        """Given a field name, return it's help text."""
        for field in self._meta.fields:
            if field.name == field_name:
                return field.help_text

    class Meta:
        model = Question
        fields = ['question', 'explaination', 'catergory']
        help_texts = {
                'question'      : ('Uw vraag uitgedrukt in een simpele zin.'),
                'explaination'  : ('Verdere uitleg over uw vraag. (Niet verplicht)'),
                'catergory'      : ('De catergorie die bij uw vraag past.'),
        }
