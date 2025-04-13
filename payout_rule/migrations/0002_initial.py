# Generated by Django 3.2.19 on 2025-04-12 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('structure', '0001_initial'),
        ('payout_rule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payoutrule',
            name='owner_structure',
            field=models.ForeignKey(limit_choices_to={'node_type': 'bank'}, on_delete=django.db.models.deletion.CASCADE, related_name='payout_rules', to='structure.structure'),
        ),
        migrations.AlterUniqueTogether(
            name='payoutrule',
            unique_together={('game_type', 'condition', 'owner_structure')},
        ),
    ]
