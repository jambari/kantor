from django.contrib import admin
from operasional.models import *
# Register your models here.



class HujanAdmin(admin.ModelAdmin):
	"""docstring for HujanAdmin"""
	list_display = ['tanggal', 'jumlah','kategori','timestamp','updated','user']
	fields = ['tanggal', 'jumlah','kategori','user']
	search_fields = ['tanggal','user__username','kategori','timestamp','updated','jumlah']
	list_filter = ['timestamp','tanggal','updated']

	class Meta:
		model = Hujan

admin.site.register(Hujan, HujanAdmin)

class GempabumiAdmin(admin.ModelAdmin):
    list_display = ['origin_time','status','magnitudo','magnitudo_type','latitude',
    				'longitude', 'depth', 'remarks', 'pga_z',
    				'pga_ns', 'pga_ew','shakemap', 'dirasakan']
    search_fields = ['origin_time','observer','latitude','longitude','magnitudo','remark']
    fieldsets = [
        (None, {
            'fields':[
                ('origin_time','status'),
                ('latitude','longitude'),
                ('magnitudo','magnitudo_type'),
                ('depth','remarks'),
                ('pga_z','pga_ns','pga_ew'),
                ('shakemap','dirasakan'),
            ]
        })
    ]
    list_filter = ()
    list_per_page = 25

admin.site.register(Gempabumi,GempabumiAdmin)

class ListrikUdaraAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'stroke','strong','noise','energy','stroke_peak',
                    'strong_peak','noise_peak','energy_peak','energy_ratio_peak',
                    'signal_peak','observer']
    search_fields = ['tanggal','observer']
    list_per_page = 25
    labels = {
        "apm_stroke": "average",
        "apm_strong": "average",
        "apm_noise": 'average',
        "apm_energy": 'average',
        "time_stroke_peak": "time",
        "time_strong_peak": "time",
        "time_noise_peak": "time",
        "time_energy_peak": "time",
        "time_ratio_peak": "time",
        "time_signal_peak": "time"
    }
    fieldsets = [
        (None, {
            'fields': ['tanggal']
        }),('Total',{
            'fields':[
                ('stroke', 'apm_stroke'),
                ('strong', 'apm_strong'),
                ('noise', 'apm_noise'),
                ('energy', 'apm_energy'),
            ]
        }),('Peak', {
            'fields': [
                ('stroke_peak', 'time_stroke_peak'),
                ('strong_peak', 'time_strong_peak'),
                ('noise_peak', 'time_noise_peak'),
                ('energy_peak', 'time_energy_peak'),
                ('energy_ratio_peak', 'time_ratio_peak'),
                ('signal_peak', 'time_signal_peak'),
            ]
        }),(None, {
            'fields': ['observer']
        })
    ]

    list_filter = ('observer', 'tanggal')

admin.site.register(ListrikUdara, ListrikUdaraAdmin)


class MagnetbumiAdmin(admin.ModelAdmin):
    list_display = ['tanggal','komponen','jam','value','rata_rata']

    list_filter = ('tanggal','komponen')
    list_per_page = 25
    search_fields = ['tanggal','komponen']
    fieldsets = [
        (None, {
            'fields': [
                ('tanggal','komponen'),
                ('jam','value','rata_rata'),
            ]
        })
    ]


admin.site.register(Magnetbumi, MagnetbumiAdmin)


class kindexAdmin(admin.ModelAdmin):
	list_display = ['tanggal','jam','value']
	list_filter = ['tanggal','jam','value']
admin.site.register(K_index, kindexAdmin)


class LaporanAdmin(admin.ModelAdmin):
    list_display = ['nama','batas_waktu','penyusun','status']
    search_fields = ['nama', 'penyusun', 'batas_waktu']
    list_filter = ('batas_waktu','penyusun', 'status')
    list_per_page = 25

admin.site.register(Laporan, LaporanAdmin)