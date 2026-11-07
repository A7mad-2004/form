from django import forms
from .models import Parson
from django import forms
from .models import Student
import os

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput,
            'university_id': forms.NumberInput,
            'national_id': forms.NumberInput,
            'mobile': forms.TextInput,
            'address': forms.TextInput,
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': forms.FileInput,
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            ext = os.path.splitext(image.name)[1].lower()
            if ext not in ['.jpg', '.jpeg', '.png']:
                raise forms.ValidationError("يُسمح فقط بصور بصيغة JPG أو PNG.")
        return image