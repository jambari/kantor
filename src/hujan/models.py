from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone

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


