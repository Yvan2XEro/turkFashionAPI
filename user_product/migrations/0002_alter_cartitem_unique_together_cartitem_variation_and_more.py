# Generated by Django 4.1.1 on 2022-09-30 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('user_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.variation'),
        ),
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('product', 'cart', 'variation')},
        ),
    ]