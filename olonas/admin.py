from django.contrib import admin
from .models import Olona


class OlonaAdmin(admin.ModelAdmin):
    list_display = (
    	'anarana',
		'fanampiny',
		'daty_nahaterahana',
		'lahy_vavy',
		'toerana_nahaterahana',
		'firenena_onenana',
		'faritra',
		'fivondronana',
		'firaisana',
		'adiresy',
		'diplaoma',
		'asa',
		)


admin.site.register(Olona, OlonaAdmin)
