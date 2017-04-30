
from django import forms
from models import Prediction

class AddPredictionForm(forms.Form):
   GPA = forms.FloatField(
       required=True,
       label="GPA",
       error_messages={'required': 'Please input GPA'},
       widget=forms.TextInput(
           attrs={
               'placeholder': "GPA",
               'class': 'form-control',
           }
       )
   )

   TOFEL = forms.FloatField(
       required=True,
       label="TOFEL",
       error_messages={'required': 'Please input TOFEL'},
       widget=forms.TextInput(
           attrs={
               'placeholder': "TOFEL",
               'class': 'form-control',
           }
       )
   )

   SATI = forms.FloatField(
       required=True,
       label="SATI",
       error_messages={'required': 'Please input SATI'},
       widget=forms.TextInput(
           attrs={
               'placeholder': "SATI",
               'class': 'form-control',
           }
       )
   )

   SchoolRankGroup = forms.ChoiceField(
       choices=list(Prediction.RANK_CHOICES),
       widget=forms.Select(
           attrs={
               'class': 'form-control',
           }
       )
   )

   Admission = forms.ChoiceField(
       choices=list(Prediction.Admission_CHOICES),
       widget=forms.Select(
           attrs={
               'class': 'form-control',
           }
       )
   )
