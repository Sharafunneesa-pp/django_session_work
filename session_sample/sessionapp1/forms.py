from django.forms import ModelForm
from . models import movies
class MovieForm(ModelForm):
    class Meta:
        model=movies
        fields='__all__'
