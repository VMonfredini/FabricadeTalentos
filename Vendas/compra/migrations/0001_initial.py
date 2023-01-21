# Generated by Django 3.1.1 on 2023-01-18 23:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('preco', models.FloatField()),
                ('tipoPagamento', models.CharField(max_length=15)),
                ('codigoRastreamento', models.CharField(max_length=15)),
                ('quantidadeComprada', models.IntegerField()),
                ('cliente_cpf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('produto_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
    ]
