from django.db import models


class Team(models.Model):

    name = models.CharField('Nome', max_length=255)
    function = models.CharField('funçao', max_length=255)
    photo = models.URLField('Foto')

    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes'

    def __str__(self):
        return self.name


class ContactUs(models.Model):

    nome = models.CharField('Nome', max_length=150)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('E-mail')
    assunto = models.CharField('Assunto', max_length=10)
    mensagem = models.TextField('Mensagem')
    criacao = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Controle de Contato'
        verbose_name_plural = 'Controle de Contatos'

    def __str__(self):
        return self.nome