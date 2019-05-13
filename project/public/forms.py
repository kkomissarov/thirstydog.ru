from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField(max_length=50)
    email.widget.attrs.update({'placeholder': 'Ваш email'})


class OrderForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=10)
    product = forms.CharField(max_length=100)

    name.widget.attrs.update({'placeholder': 'Ваше имя', 'autocomplete': 'off'})
    phone.widget.attrs.update({'placeholder': 'Ваш телефон', 'autocomplete': 'off'})
