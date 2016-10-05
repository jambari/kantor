# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 13:48
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tatausaha', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gempabumi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('automatic', 'automatic'), ('manual', 'manual')], max_length=50)),
                ('magnitudo', models.SmallIntegerField()),
                ('magnitudo_type', models.CharField(max_length=15)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('depth', models.SmallIntegerField()),
                ('remarks', models.CharField(blank=True, max_length=250)),
                ('pga_z', models.FloatField(default=0)),
                ('pga_ns', models.FloatField(default=0)),
                ('pga_ew', models.FloatField(default=0)),
                ('shakemap', models.BooleanField(default=False)),
                ('dirasakan', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['origin_time'],
                'verbose_name_plural': 'Gempabumi',
            },
        ),
        migrations.CreateModel(
            name='Hujan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('jumlah', models.FloatField(default=0, null=True)),
                ('kategori', models.CharField(choices=[('nihil', 'nihil'), ('sangat ringan', 'sangat ringan'), ('ringan', 'ringan'), ('sedang', 'sedang'), ('lebat', 'lebat'), ('sangat lebat', 'sangat lebat')], max_length=50)),
                ('keterangan', models.CharField(blank=True, max_length=255, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['tanggal'],
                'verbose_name_plural': 'Hujan',
            },
        ),
        migrations.CreateModel(
            name='Laporan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=200)),
                ('batas_waktu', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('penyusun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tatausaha.Pegawai')),
            ],
            options={
                'ordering': ['batas_waktu'],
                'verbose_name_plural': 'Laporan',
            },
        ),
        migrations.CreateModel(
            name='LaporanShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('lemi', models.BooleanField(default=False)),
                ('seiscomp3', models.BooleanField(default=False)),
                ('accelero', models.BooleanField(default=False)),
                ('LD2000', models.BooleanField(default=False)),
                ('jumlah_event', models.SmallIntegerField(default=0)),
                ('variasi_harian', models.BooleanField(default=False)),
                ('prekursor', models.BooleanField(default=False)),
                ('pasang_pias', models.BooleanField(default=False)),
                ('sample_hujan', models.BooleanField(default=False, verbose_name='ARWS')),
                ('note_for_next_shift', models.CharField(blank=True, max_length=250)),
                ('keterangan', models.CharField(blank=True, max_length=250)),
                ('petugas', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['tanggal'],
                'verbose_name_plural': 'Laporan Shift',
            },
        ),
        migrations.CreateModel(
            name='ListrikUdara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(default=datetime.datetime.today)),
                ('stroke', models.IntegerField(blank=True, default=0, null=True)),
                ('apm_stroke', models.FloatField(default=0.0, verbose_name='average')),
                ('strong', models.IntegerField(blank=True, default=0, null=True)),
                ('apm_strong', models.FloatField(default=0.0, verbose_name='average')),
                ('noise', models.IntegerField(blank=True, default=0, null=True)),
                ('apm_noise', models.FloatField(default=0.0, verbose_name='average')),
                ('energy', models.IntegerField(blank=True, default=0, null=True)),
                ('apm_energy', models.FloatField(default=0.0, verbose_name='average')),
                ('stroke_peak', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('time_stroke_peak', models.TimeField(blank=True, default='00:00:00')),
                ('strong_peak', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('time_strong_peak', models.TimeField(blank=True, default='00:00:00')),
                ('noise_peak', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('time_noise_peak', models.TimeField(blank=True, default='00:00:00')),
                ('energy_peak', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('time_energy_peak', models.TimeField(blank=True, default='00:00:00')),
                ('energy_ratio_peak', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('time_ratio_peak', models.TimeField(blank=True, default='00:00:00')),
                ('signal_peak', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('time_signal_peak', models.TimeField(blank=True, default='00:00:00')),
                ('observer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['tanggal'],
                'verbose_name_plural': 'Listrik Udara',
            },
        ),
        migrations.CreateModel(
            name='Magnetbumi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('jam', models.CharField(choices=[('00', '00'), ('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23')], max_length=2)),
                ('komponen', models.CharField(blank=True, choices=[('X', 'X'), ('Y', 'Y'), ('Z', 'Z'), ('H', 'H'), ('D', 'D'), ('I', 'I'), ('F', 'F')], max_length=2)),
                ('value', models.FloatField()),
                ('rata_rata', models.FloatField()),
            ],
            options={
                'ordering': ['tanggal'],
                'verbose_name_plural': 'Magnetbumi',
            },
        ),
    ]
