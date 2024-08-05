from django import forms


class ItemSearchForm(forms.Form):
    tombo = forms.IntegerField(label='Tombo', required=True)

