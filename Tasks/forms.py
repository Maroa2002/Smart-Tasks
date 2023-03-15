from django import forms
from .models import Tasks

class TasksForm(forms.ModelForm):
    # task_type = forms.ModelChoiceField(queryset=TaskType.objects, empty_label=None)

    class Meta:
        model = Tasks
        fields = ('task_title', 'task_type', 'task_details', 'due_date')
        widgets = {
            'task_title': forms.TextInput(attrs={'class': '-5 rounded'}),
            'task_details': forms.Textarea(attrs={'class': 'mt-5 h-16'}),
        }
        labels = {
            'task_title': 'Enter Task',
            'task_details': 'What is to be done?',
            'due_date': 'Due date'
        }