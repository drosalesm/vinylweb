from django import forms
from applications.landing.models import *

class opt_navbar_form(forms.ModelForm):
    class Meta:
        model = nav_bar_opt
        fields = ('__all__')


class tracks_form(forms.ModelForm):
    class Meta:
        model = tracks
        fields = ('__all__')


class bio_form(forms.ModelForm):
    class Meta:
        model = biografia
        fields = ('__all__')

class contact_form(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ('__all__')

class vivo_form(forms.ModelForm):
    class Meta:
        model = en_vivo
        fields = ('__all__')





