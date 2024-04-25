from django import forms
from .models import Task


CHOICE_PRIORITY = (
    (0, 'Alto'),
    (1, 'Médio'),
    (2, 'Baixo'),
)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'limite_date', 'priority']

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome da Tarefa...'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Descrição da Tarefa...'}))
    limite_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input', 'type': 'date'}))
    priority = forms.ChoiceField(widget=forms.Select(attrs={'class': 'select input'}), choices=CHOICE_PRIORITY)
