from django import forms 
import datetime


GENDER_CHOICES = (
('M', 'Male'),
('F', 'Female'),
)

class DataRowForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices = GENDER_CHOICES)
    favorite_number = forms.IntegerField()