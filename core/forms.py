from django import forms


class CalculateForm(forms.Form):
    num_one = forms.IntegerField(
        label='a'
    )

    num_two = forms.IntegerField(
        label='b'
    )

    num_three = forms.IntegerField(
        label='c'
    )
