# Generated by Django 4.2.3 on 2023-07-20 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_type', models.CharField(max_length=100)),
                ('event_description', models.TextField(max_length=500)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ticket_quantity', models.PositiveIntegerField()),
                ('venue_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='tickit.venue')),
            ],
        ),
    ]
