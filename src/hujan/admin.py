from django.contrib import admin
from hujan.models import Hujan
# Register your models here.

class HujanAdmin(admin.ModelAdmin):
	"""docstring for HujanAdmin"""
	list_display = ['tanggal', 'jumlah','kategori','timestamp','updated','user']
	fields = ['tanggal', 'jumlah','kategori','user']
	search_fields = ['tanggal','user']
	list_filter = ['timestamp','tanggal','updated']

	class Meta:
		model = Hujan

admin.site.register(Hujan, HujanAdmin)

