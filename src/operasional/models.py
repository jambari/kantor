from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from tatausaha.models import *
from django.db.models.signals import pre_save
# Create your models here.



class Hujan(models.Model):
	"""Mendefinisikan tabel Hujan"""

	kategori_choices = (
		('nihil', 'nihil'),
		('sangat ringan', 'sangat ringan'),
		('ringan','ringan'),
		('sedang','sedang'),
		('lebat','lebat'),
		('sangat lebat', 'sangat lebat'),
		)

	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	tanggal = models.DateField(auto_now=False, auto_now_add=False)
	jumlah = models.FloatField(null=True, default=0)
	kategori = models.CharField(max_length=50, choices=kategori_choices)
	keterangan = models.CharField(max_length=255, blank=True, null = True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    #timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return str(self.tanggal)

	def __unicode__(self):
		return str(self.tanggal)

	class Meta:
		verbose_name_plural = "Hujan"
		ordering = ['tanggal']


class Gempabumi(models.Model):
    """(Gempabumi description)"""
    status_choices = (
    	('automatic','automatic'),
    	('manual','manual')
    	)
    origin_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=50, choices=status_choices)
    magnitudo = models.SmallIntegerField()
    magnitudo_type = models.CharField(max_length=15)
    latitude = models.FloatField()
    longitude = models.FloatField()
    depth = models.SmallIntegerField()
    remarks = models.CharField(max_length=250, blank=True)
    pga_z = models.FloatField(default = 0)
    pga_ns = models.FloatField(default = 0)
    pga_ew = models.FloatField(default = 0)
    shakemap = models.BooleanField(default=False)
    dirasakan = models.BooleanField(default=False)

    class Meta:
        ordering = ['origin_time']
        verbose_name_plural = 'Gempabumi'

    def __str__(self):
        return str(self.tanggal)+" "+ str(self.origin_time)

    def __unicode__(self):
        return str(self.tanggal)+" "+ str(self.origin_time)


class ListrikUdara(models.Model):
    """(ListrikUdara description)"""
    tanggal = models.DateField(default=datetime.datetime.today)
    stroke = models.IntegerField(blank=True, null=True, default=0)
    apm_stroke = models.FloatField(default=0.0, verbose_name = 'average')
    strong = models.IntegerField(blank=True, null=True, default=0)
    apm_strong = models.FloatField(default=0.0, verbose_name = 'average')
    noise = models.IntegerField(blank=True, null=True, default=0)
    apm_noise = models.FloatField(default=0.0, verbose_name = 'average')
    energy = models.IntegerField(blank=True, null=True, default=0)
    apm_energy = models.FloatField(default=0.0, verbose_name = 'average')
    stroke_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_stroke_peak = models.TimeField(blank=True, default='00:00:00')
    strong_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_strong_peak = models.TimeField(blank=True, default='00:00:00')
    noise_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_noise_peak = models.TimeField(blank=True, default='00:00:00')
    energy_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_energy_peak = models.TimeField(blank=True, default='00:00:00')
    energy_ratio_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_ratio_peak = models.TimeField(blank=True, default='00:00:00')
    signal_peak = models.PositiveIntegerField(blank=True, null=True, default=0)
    time_signal_peak = models.TimeField(blank=True, default='00:00:00')
    observer = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def __str__(self):
        return str(self.tanggal)


    def __unicode__(self):
        return str(self.tanggal)

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Listrik Udara'



class Magnetbumi(models.Model):
    """model for magnet bumi yang sudah dirata2kan perjam"""
    KOMPONEN_CHOICES = (
        ('X', 'X'),
        ('Y', 'Y'),
        ('Z', 'Z'),
        ('H', 'H'),
        ('D', 'D'),
        ('I', 'I'),
        ('F', 'F'),
    )

    jam_choices = (
    	('00','00'),('01','01'),('02','02'),('03','03'),
    	('04','04'),('05','05'),('06','06'),('07','07'),
    	('08','08'),('09','09'),('10','10'),('11','11'),
    	('12','12'),('13','13'),('14','14'),('15','15'),
    	('16','16'),('17','17'),('18','18'),('19','19'),
    	('20','20'),('21','21'),('22','22'),('23','23'),
    	)
    tanggal = models.DateField()
    jam = models.CharField(max_length=2, choices=jam_choices)
    komponen = models.CharField(blank=True, max_length=2, choices = KOMPONEN_CHOICES)
    value = models.FloatField()
    
    rata_rata = models.FloatField()


    def __str__(self):
        return str(self.tanggal)

    def __unicode__(self):
        return self.tanggal

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Magnetbumi'

class K_index(models.Model):
	"""model K index"""
	jam_index_choices = (
		('00-03','00-03'),('03-06','03-06'),
		('06-09','06-09'),('09-12','09-12'),
		('12-15','12-15'),('15-18','15-18'),
		('18-21','18-21'),('21-24','21-24')
		)
	tanggal = models.DateField(auto_now=False, auto_now_add=False)
	jam = models.CharField(max_length=3, choices=jam_index_choices)
	value = models.SmallIntegerField(default=0.0)




class Laporan(models.Model):
    """(Laporan description)"""
    nama = models.CharField(blank=True, max_length=200)
    batas_waktu = models.DateField()
    penyusun = models.ForeignKey(Pegawai)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

    def __unicode__(self):
        return self.nama

    class Meta:
        ordering = ['batas_waktu']
        verbose_name_plural = 'Laporan'


class LaporanShift(models.Model):
	tanggal = models.DateField(auto_now=False, auto_now_add=False)
	lemi = models.BooleanField(default=False)
	seiscomp3 = models.BooleanField(default=False)
	accelero = models.BooleanField(default=False)
	LD2000 = models.BooleanField(default=False)
	jumlah_event = models.SmallIntegerField(default=0)
	variasi_harian = models.BooleanField(default=False)
	prekursor = models.BooleanField(default=False)
	pasang_pias = models.BooleanField(default=False)
	sample_hujan = models.BooleanField(default=False, verbose_name='ARWS')
	note_for_next_shift = models.CharField(max_length=250, blank=True)
	keterangan = models.CharField(max_length=250, blank=True)
	petugas = models.CharField(max_length=250, blank=False)

	def __str__(self):
		return str(self.tanggal)

	def __unicode__(self):
		return str(self.tanggal)

	class Meta:
		ordering = ['tanggal']
		verbose_name_plural = 'Laporan Shift'