# Generated by Django 4.2.4 on 2023-09-16 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('gramme', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('calories', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('carbohydrates', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fat', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientQuantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet_models.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('ingredients', models.ManyToManyField(through='diet_models.IngredientQuantity', to='diet_models.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeofDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Śniadanie', 'Śniadanie'), ('Obiad', 'Obiad'), ('Kolacja', 'Kolacja')])),
            ],
        ),
        migrations.CreateModel(
            name='MealTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Poniedziałek', 'Poniedziałek'), ('Wtorek', 'Wtorek'), ('Środa', 'Środa'), ('Czwartek', 'Czwartek'), ('Piątek', 'Piątek'), ('Sobota', 'Sobota'), ('Niedziela', 'Niedziela')])),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet_models.meal')),
                ('timeofday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet_models.timeofday')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ingredientquantity',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diet_models.meal'),
        ),
        migrations.CreateModel(
            name='BMI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmi', models.CharField(max_length=10)),
                ('healthy_bmi_range', models.CharField(max_length=100)),
                ('health', models.CharField(max_length=100)),
                ('weight', models.CharField(default='0', max_length=64)),
                ('height', models.CharField(default='0', max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]