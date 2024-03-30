from django import forms


class SearchEventForm(forms.Form):
    search_by = forms.CharField(max_length=100)
