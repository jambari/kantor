from django.contrib import admin
from tatausaha.models import *
# Register your models here.

class DivisiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'keterangan']
    search_fields = ['nama']
    list_per_page = 25
    list_filter = ()

admin.site.register(Divisi, DivisiAdmin)

class JabatanAdmin(admin.ModelAdmin):
    list_display = ['nama','keterangan']
    search_fields = ['nama']
    list_per_page = 25
    list_filter = ()

admin.site.register(Jabatan, JabatanAdmin)

class PegawaiAdmin(admin.ModelAdmin):
    list_display = ['nama','tempat_lahir','nip','alamat','golongan','jabatan','email','status', 'created']
    fieldsets = [
        (None,{
            'fields': ['nama']
        }),(None, {
            'fields':['alamat','nip']
        }),(None,{
            'fields':['tempat_lahir','tanggal_lahir']
        }),(None,{
            'fields': ['pangkat', 'golongan']
        }),(None,{
            'fields': ['jabatan','pendidikan_terakhir']
        }),(None,{
            'fields': ['email','nomor_rekening']
        }),(None, {
            'fields': ['agama', 'bagian']
        }),(None,{
            'fields': ['status']
        })
    ]

    list_per_page = 25
    search_fields = ['nama', 'nip']
    list_filter = ()


admin.site.register(Pegawai, PegawaiAdmin)

class JenisAkunAdmin(admin.ModelAdmin):
    list_display = ['akun', 'pegawai', 'jenis_akun']
    list_per_page = 25
    search_fields = ['akun','pegawai', 'jenis_akun']
    list_filter=()

admin.site.register(JenisAkun, JenisAkunAdmin)


#Admin Surat Keluar
class SuratKeluarAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'nomor_surat', 'perihal', 'tujuan', 'keterangan', 'petugas_entri']
    list_per_page = 25
    search_fields = ('tanggal', 'nomor_surat', 'perihal', 'tujuan', 'petugas_entri')
    list_filter=()

admin.site.register(SuratKeluar, SuratKeluarAdmin)

#Admin Surat MASUK
class SuratMasukAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'nomor_surat', 'perihal', 'dari', 'keterangan', 'petugas_entri']
    list_per_page = 25
    search_fields = ['tanggal', 'nomor_surat', 'perihal', 'dari','petugas_entri']
    list_filter = ()

admin.site.register(SuratMasuk, SuratMasukAdmin)

#Admin AlatTulisKantor
class AlatTulisKantorAdmin(admin.ModelAdmin):
    list_display = ['tanggal','nama_barang','jumlah', 'keterangan','petugas','petugas_entri']
    search_fields = ['tanggal','nama_barang','jumlah','petugas','petugas_entri']
    list_per_page = 25
    list_filter = ()

admin.site.register(AlatTulisKantor, AlatTulisKantorAdmin)

#admin Diklat
class DiklatAdmin(admin.ModelAdmin):
    list_display = ['nama_diklat','nama_peserta','waktu_mulai','waktu_berakhir','lokasi','presentasi','petugas_entri']
    list_filter = ()
    search_fields = ['nama_diklat', 'nama_peserta', 'waktu_mulai', 'waktu_berakhir']
    list_per_page = 25

admin.site.register(Diklat, DiklatAdmin)

class ListrikMatiAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'jam_mulai', 'jam_berakhir', 'kondisi_bbm', 'keterangan', 'petugas_entri']
    list_per_page = 25
    search_fields = ['tanggal']

admin.site.register(ListrikMati,ListrikMatiAdmin)

class MemoAdmin(admin.ModelAdmin):
    list_display = ['tanggal','judul','dari','kepada','status','petugas_entri']
    list_per_page = 25
    search_fields = ['tanggal', 'judul', 'dari', 'kepada']
    list_filter = ()

admin.site.register(Memo, MemoAdmin)

class JadwalDinasSatpamAdmin(admin.ModelAdmin):
    list_display = ['tanggal', 'pegawai', 'keterangan', 'petugas_entri']
    search_fields = ['tanggal', 'pegawai']
    list_per_page = 25
    list_filter = ()

admin.site.register(JadwalDinasSatpam, JadwalDinasSatpamAdmin)

class TugasBelajarAdmin(admin.ModelAdmin):
    list_display = ['pegawai','program','jurusan','perguruan_tinggi', 'tahun_mulai','tahun_lulus', 'petugas_entri']
    search_fields = ['pegawai','program','jurusan','perguruan_tinggi','tahun_mulai','tahun_lulus']
    list_per_page = 25
    list_filter = ()

admin.site.register(TugasBelajar, TugasBelajarAdmin)
