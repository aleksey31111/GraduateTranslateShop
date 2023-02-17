from django import forms
from captcha.fields import CaptchaField


class DesignForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        min_length=3,
        max_length=200,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя',
                   'class': 'form-input'}
        )
    )
    email = forms.EmailField(
        label='e-mail',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Электронная почта'}
        )
    )
    number_card = forms.IntegerField(
        # max_value=9999999999999999,
        # min_value=0000000000000000,
        widget=forms.NumberInput(
            attrs={'placeholder': 'Номер вашей карты',
                   'class': 'form-input'}
        )
    )
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super(DesignForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control py-4"

    class Meta:
        # model = User
        fields = ('name', 'email', 'number_cart', 'captcha')
