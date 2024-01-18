from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = DepartmentModel
        fields = "__all__"