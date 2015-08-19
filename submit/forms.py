__author__ = 'MillerB'

from django import forms


class SubmitForm(forms.Form):
    code = forms.IntegerField(label="Song Code:",
                              widget=forms.NumberInput(attrs={'placeholder': 'enter number',
                                                              'step': '1'}))
    title = forms.CharField(label="Title:", max_length=50,
                            widget=forms.TextInput(attrs={'placeholder': 'enter text',
                                                          'autocomplete': 'off'}))
    artist = forms.CharField(label="Artist:", max_length=50,
                             widget=forms.TextInput(attrs={'placeholder': 'enter text',
                                                           'autocomplete': 'off'}))
    company = forms.ChoiceField(label="Company:",
                                choices=(
                                    (None, 'Select..'),
                                    ('TJ Media', 'TJ Media'),
                                    ('Kumyoung', 'Kumyoung'),
                                    ('Platinum', 'Platinum'),
                                ))