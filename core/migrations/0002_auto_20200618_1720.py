# Generated by Django 3.0.7 on 2020-06-18 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('D', 'Drinks'), ('FW', 'Female Wear'), ('MW', 'Men Wear'), ('K', 'Kids'), ('SW', 'Sport wear'), ('OW', 'Outwear')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('L', 'limited'), ('O', 'out of stock'), ('P', 'premium')], max_length=1),
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
            ],
            options={
                'unique_together': {('item', 'name')},
            },
        ),
        migrations.CreateModel(
            name='ItemVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('attachment', models.ImageField(blank=True, upload_to='')),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Variation')),
            ],
            options={
                'unique_together': {('variation', 'value')},
            },
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item_variations',
            field=models.ManyToManyField(to='core.ItemVariation'),
        ),
    ]
