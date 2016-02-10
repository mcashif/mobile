from django import forms
from .models import DriverJob, Client, Driver

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['name', 'phone',]


class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ['name', 'phone', 'address',]

class WorkForm(forms.ModelForm):

    class Meta:
        model = DriverJob
        fields = ['clientid', 'driverid', 'instructions',]
