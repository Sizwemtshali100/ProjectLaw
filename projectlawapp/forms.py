from . models import ProjectLawModel
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class ProjectLawForms(ModelForm):
    class Meta:
        fields = ['TheCompany','TheClient','TheFile']
        model = ProjectLawModel
