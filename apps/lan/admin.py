# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin

from apps.lan.models import LAN, TicketType, TicketTypeTranslation, LANTranslation, Ticket

class LANTranslationInlineAdmin(admin.StackedInline):
    verbose_name = "Translation"
    verbose_name_plural = "Translations"
    model = LANTranslation
    max_num = len(settings.LANGUAGES)
    extra = 2

class LANAdmin(admin.ModelAdmin):
    model = LAN
    list_display = ['title', 'location', 'start_date', 'end_date',]
    inlines = [LANTranslationInlineAdmin,]


class TicketTypeTranslationInlineAdmin(admin.StackedInline):
    verbose_name = "Translation"
    verbose_name_plural = "Translations"
    model = TicketTypeTranslation
    max_num = len(settings.LANGUAGES)
    extra = 2


class TicketTypeAdmin(admin.ModelAdmin):
    model = TicketType
    inlines = [TicketTypeTranslationInlineAdmin,]
    list_display = ['__unicode__', 'lan', 'number_of_seats', 'price',]


class TicketAdmin(admin.ModelAdmin):
	model = Ticket

admin.site.register(LAN, LANAdmin)
admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Ticket, TicketAdmin)
