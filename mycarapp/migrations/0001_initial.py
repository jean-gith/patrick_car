# Generated by Django 3.1.5 on 2021-01-31 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('comid', models.AutoField(primary_key=True, serialize=False)),
                ('comnom', models.CharField(max_length=250)),
                ('comprenom', models.CharField(max_length=250)),
                ('comemail', models.EmailField(max_length=254)),
                ('comavis', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('inscrisid', models.AutoField(primary_key=True, serialize=False)),
                ('inscrisnom', models.CharField(max_length=250)),
                ('inscrisprenom', models.CharField(max_length=250)),
                ('inscrisphone', models.IntegerField()),
                ('inscrisemail', models.EmailField(max_length=254)),
                ('inscrismdp', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('carid', models.AutoField(primary_key=True, serialize=False)),
                ('carnom', models.CharField(max_length=50)),
                ('carsprix', models.IntegerField()),
                ('carpassager', models.IntegerField()),
                ('carmoteur', models.CharField(max_length=50)),
                ('carporte', models.IntegerField()),
                ('carcarburant', models.CharField(max_length=50)),
                ('carcategorie', models.CharField(max_length=50)),
                ('caroption', models.CharField(max_length=100)),
                ('carimg', models.ImageField(upload_to='')),
                ('carimg1', models.ImageField(upload_to='')),
                ('carimg2', models.ImageField(upload_to='')),
                ('carimg3', models.ImageField(upload_to='')),
                ('carimg4', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('rsvid', models.AutoField(primary_key=True, serialize=False)),
                ('rsvlieuramassage', models.CharField(max_length=150)),
                ('rsvdateramassage', models.DateTimeField()),
                ('rsvlieuretour', models.CharField(max_length=150)),
                ('rsvdateretour', models.DateTimeField()),
                ('rsvnomreservant', models.CharField(max_length=150)),
                ('rsvprennomreservant', models.CharField(max_length=150)),
                ('rsvmailreservant', models.EmailField(max_length=150)),
                ('rsvphonereservant', models.IntegerField()),
                ('rsvsupinfo', models.CharField(max_length=250)),
                ('rsvoiture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycarapp.voiture')),
            ],
        ),
    ]
