from django import forms
from django.forms import ModelForm
from .models import Tasks

class TasksForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'Placeholder':'Add New Task...'}))

    class Meta:
        model = Tasks
        fields = '__all__'