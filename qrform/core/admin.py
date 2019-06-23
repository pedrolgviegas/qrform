from django.contrib import admin
from django.utils.html import format_html
from django.utils.timezone import now
from qrform.core.models import ContactUs, Team

class TeamModelAdmin(admin.ModelAdmin):

    list_display = ('name', 'function', 'photo')

    def website_link(self, obj):

        return format_html('<a href="{0}">{0}</a>'.format(obj.website))

    website_link.allow_tags = True
    website_link.short_description = 'website'


    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}" />'.format(obj.photo))

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

class ContactUsModelAdmin(admin.ModelAdmin):

    list_display = ('nome', 'telefone', 'email', 'assunto', 'mensagem', 'criacao', 'criado_hoje')
    date_hierarchy = 'criacao'

    #informa prioridade de campos de busca (não precisa informar todos, apenas os que achar que precisa)
    search_fields = ('nome', 'telefone', 'email', 'assunto', 'mensagem', 'criacao')

    def criado_hoje(self, obj):
        return obj.criacao.date() == now().date()

    criado_hoje.short_description = 'Criado Hoje?'

    criado_hoje.boolean = True

admin.site.register(ContactUs, ContactUsModelAdmin)
admin.site.register(Team, TeamModelAdmin)