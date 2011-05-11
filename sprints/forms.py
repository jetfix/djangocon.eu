from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant