# Generated by Django 3.2.12 on 2022-05-13 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('valid_period', models.SmallIntegerField(choices=[(1, '1天'), (3, '3天'), (7, '1周'), (14, '2周'), (30, '1个月'), (60, '2个月'), (90, '3个月'), (180, '6个月'), (210, '12个月'), (540, '18个月'), (720, '24个月')])),
                ('price', models.FloatField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]