from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Divisi(models.Model):
    """(Divisi description)"""
    nama = models.CharField(blank=True, max_length=100)
    keterangan = models.TextField(blank=True)

    class Meta:
        ordering = ['nama']
        verbose_name_plural = 'Divisi'

    def __unicode__(self):
        return self.nama

    def __str__(self):
        return self.nama


class Jabatan(models.Model):
    """(Divisi description)"""
    nama = models.CharField(blank=True, max_length=100)
    keterangan = models.TextField(blank=True)

    class Meta:
        ordering = ['nama']
        verbose_name_plural = 'Jabatan'

    def __unicode__(self):
        return self.nama

    def __str__(self):
        return self.nama



class Pegawai(models.Model):
    AGAMA_CHOICES = (
        ('Islam', 'Islam'),
        ('Protestan', 'Protestan'),
        ('Katolik', 'Katolik'),
        ('Hindu', 'Hindu'),
        ('Budha', 'Budha'),
        ('Konghuchu', 'Konghuchu'),
    )

    STATUS_CHOICES = (
        ('PNS', 'PNS'),
        ('CPNS', 'CPNS'),
        ('Honor', 'Honor'),
        ('Magang', 'Magang'),
    )

    """(Pegawai description)"""
    nama = models.CharField(max_length = 255)
    alamat = models.TextField(blank=True)
    nip = models.CharField(blank=True, max_length=100)
    tempat_lahir = models.CharField(blank=True, max_length=100)
    tanggal_lahir = models.DateField(auto_now = False)
    pangkat = models.CharField(blank=True, max_length=100)
    golongan = models.CharField(blank=True, max_length=15)
    jabatan = models.ForeignKey(Jabatan)
    pendidikan_terakhir = models.CharField(blank=True, max_length=100)
    email = models.EmailField()
    nomor_rekening = models.CharField(blank=True, max_length=100)
    agama = models.CharField(blank=True, max_length=100, choices=AGAMA_CHOICES)
    bagian = models.ForeignKey(Divisi)
    status = models.CharField(blank=True, max_length=100, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['nama']
        verbose_name_plural = 'Pegawai'

    def __unicode__(self):
        return self.nama

    def __str__(self):
        return self.nama

class JenisAkun(models.Model):
    """(JenisPegawai description)"""

    JENIS_AKUN_CHOICES = (
        ('pegawai','Pegawai'),
        ('admin', 'admin'),
    )
    akun = models.ForeignKey(User)
    pegawai = models.ForeignKey(Pegawai)
    jenis_akun = models.CharField(max_length=50, choices=JENIS_AKUN_CHOICES)

    class Meta:
        verbose_name_plural = 'Jenis Akun'

    def __unicode__(self):
        return str(self.akun)

    def __str__(self):
        return str(self.akun)



#SURAT MASUK
class SuratKeluar(models.Model):
    tanggal = models.DateField(default=datetime.datetime.today)
    nomor_surat = models.CharField(blank=True, max_length=100)
    perihal = models.CharField(blank=True, max_length=100)
    tujuan = models.CharField(blank=True, max_length=100)
    keterangan = models.TextField(blank=True)
    petugas_entri = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Surat Keluar'

    def __str__(self):
        return self.nomor_surat

    def __unicode__(self):
        return self.nomor_surat


class SuratMasuk(models.Model):
    tanggal = models.DateField(default=datetime.datetime.today)
    nomor_surat = models.CharField(blank=True, max_length=100)
    perihal = models.CharField(blank=True, max_length=100)
    dari = models.CharField(blank=True, max_length=100)
    keterangan = models.TextField(blank=True)
    petugas_entri = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Surat Masuk'

    def __str__(self):
        return self.nomor_surat

    def __unicode__(self):
        return self.nomor_surat


class AlatTulisKantor(models.Model):
    tanggal = models.DateField(default=datetime.datetime.today)
    nama_barang = models.CharField(blank=True, max_length=100)
    jumlah = models.CharField(blank=True, max_length=100)
    keterangan = models.TextField(blank=True)
    petugas = models.ForeignKey(Pegawai)
    petugas_entri = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Alat Tulis Kantor'

    def __str__(self):
        return self.nama_barang

    def __unicode__(self):
        return self.nama_barang

class Diklat(models.Model):
    nama_diklat = models.CharField(blank=True, max_length=100)
    nama_peserta = models.ForeignKey(Pegawai)
    waktu_mulai = models.DateField(default=datetime.datetime.today)
    waktu_berakhir = models.DateField(default=datetime.datetime.today)
    lokasi = models.CharField(blank=True, max_length=100)
    presentasi = models.BooleanField(default=False)
    petugas_entri = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    class Meta:
        ordering = ['waktu_mulai', 'nama_diklat']
        verbose_name_plural = 'Diklat'

    def __str__(self):
        return self.nama_diklat

    def __unicode__(self):
        return self.nama_diklat

class ListrikMati(models.Model):
    tanggal = models.DateField(default=datetime.datetime.today)
    jam_mulai = models.TimeField(blank=True)
    jam_berakhir = models.TimeField(blank=True)
    kondisi_bbm = models.CharField(blank=True, max_length=100)
    keterangan = models.TextField(blank=True)
    petugas_entri = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Listrik Mati'

    def __str__(self):
        return str(self.tanggal)

    def __unicode__(self):
        return str(self.tanggal)


class Memo(models.Model):
    tanggal = models.DateField(default=datetime.datetime.today)
    judul = models.CharField(blank=True, max_length=100)
    dari = models.CharField(blank=True, max_length=100)
    kepada = models.CharField(blank=True, max_length=100)
    isi_memo = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    petugas_entri = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Memo'

    def __str__(self):
        return self.judul

    def __unicode__(self):
        return self.judul


class JadwalDinasSatpam(models.Model):
    KETERANGAN_CHOICES = (
        ('Pagi', 'Pagi'),
        ('Siang', 'Siang'),
        ('Malam', 'Malam')
    )
    tanggal = models.DateField(default=datetime.datetime.today)
    pegawai = models.ForeignKey(Pegawai)
    keterangan = models.CharField(blank=True, max_length=100, choices=KETERANGAN_CHOICES)
    petugas_entri = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Jadwal Dinas Satpam'

    def __str__(self):
        return str(self.tanggal)

    def __unicode__(self):
        return str(self.tanggal)


class TugasBelajar(models.Model):
    PROGRAM_CHOICES = (
        ('Diploma 4', 'Diploma 4'),
        ('Sarjana', 'Sarjana'),
        ('Magister', 'Magister'),
        ('Doctoral', 'Doctoral'),
    )

    pegawai = models.ForeignKey(Pegawai)
    program = models.CharField(blank=True, max_length=100, choices=PROGRAM_CHOICES)
    jurusan = models.CharField(blank=True, max_length=100)
    perguruan_tinggi = models.CharField(blank=True, max_length=200)
    tahun_mulai = models.PositiveIntegerField(blank=True, null=True)
    tahun_lulus = models.PositiveIntegerField(blank=True, null=True)
    keterangan = models.CharField(blank=True, max_length=200)
    petugas_entri = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    class Meta:
        ordering = ['pegawai']
        verbose_name_plural = 'Tugas Belajar'

    def __str__(self):
        return str(self.pegawai)

    def __unicode__(self):
        return str(self.pegawai)
