from django import forms
from testapp.models import Student

class StudentForm(forms.ModelForm):
    def clean_mark(self):
        inputmark = self.cleaned_data['mark']
        if inputmark < 35:
            raise forms.ValidationError('Mark Shoud be >= 35')
        return inputmark
    class Meta:
        model = Student
        fields = '__all__'
