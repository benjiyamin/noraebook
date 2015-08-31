__author__ = 'MillerB'

from django import forms


class SubmitForm(forms.Form):
    code = forms.IntegerField(required=True,
                              widget=forms.NumberInput(attrs={'placeholder': 'Song Code',
                                                              'step': '1'}))
    title = forms.CharField(max_length=50, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Title',
                                                          'autocomplete': 'off'}))
    artist = forms.CharField(max_length=50, required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Artist',
                                                           'autocomplete': 'off'}))
    company = forms.ChoiceField(label="Company:",
                                choices=(
                                    (None, 'Select Company..'),
                                    ('TJ Media', 'TJ Media'),
                                    ('Kumyoung', 'Kumyoung'),
                                    ('Platinum', 'Platinum'),
                                ))