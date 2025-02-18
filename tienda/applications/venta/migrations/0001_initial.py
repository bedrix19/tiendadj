# Generated by Django 5.0.7 on 2024-07-17 12:53

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date_sale', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Venta')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto')),
                ('count', models.PositiveIntegerField(verbose_name='Cantidad de Productos')),
                ('type_invoce', models.CharField(choices=[('0', 'BOLETA'), ('3', 'FACTURA'), ('4', 'OTRO')], max_length=2, verbose_name='TIPO')),
                ('cancelado', models.BooleanField(default=False)),
                ('type_payment', models.CharField(choices=[('0', 'TARJETA'), ('1', 'DEPOSITO'), ('2', 'CONTRAENTREGA')], max_length=2, verbose_name='TIPO PAGO')),
                ('state', models.CharField(blank=True, choices=[('0', 'En Proceso'), ('1', 'En Envio'), ('2', 'En Tienda'), ('3', 'Entregado')], max_length=2, verbose_name='Estado de Envio')),
                ('adreese_send', models.TextField(blank=True, verbose_name='Direccion de Envio')),
                ('anulate', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_venta', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'ventas',
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('count', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('price_purchase', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Precio Compra')),
                ('price_sale', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Venta')),
                ('anulate', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.sale', verbose_name='Codigo de Venta')),
            ],
            options={
                'verbose_name': 'Detalle Venta',
                'verbose_name_plural': 'Detalles de una Venta',
            },
        ),
    ]
