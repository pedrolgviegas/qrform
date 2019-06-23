from django import forms

class CoreForm(forms.Form):

    nome = forms.CharField(label='Nome* ',
                           widget=forms.TextInput(
                               attrs={'class': 'caixa', 'placeholder': 'Nome', 'id': 'nome'}))

    telefone = forms.CharField(label='Telefone ',
                           widget=forms.TextInput(
                               attrs={'class': 'caixa', 'placeholder': '(XX) XXXXX-XXXX', 'id':'phone'}))

    email = forms.CharField(label='Email ',
                               widget=forms.EmailInput(
                                   attrs={'class': 'caixa', 'placeholder': 'Email', 'id': 'caixaemail'}))

    assunto = forms.CharField(label='Assunto ',
                               widget=forms.TextInput(
                                   attrs={'class': 'caixa', 'placeholder': 'Informe o assunto', 'id': 'caixaselect'}))
                                   #ChoiceField(choices=('0', '---selecione---')))

    mensagem = forms.CharField(label='mensagem ',
                               widget=forms.Textarea(
                                attrs={'class': 'area', 'placeholder': 'Digite seu texto aqui', 'id': 'textarea',
                                       'cols': '40', 'rows': '7', 'style': 'resize:horizontal'}))