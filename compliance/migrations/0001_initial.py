# Generated by Django 2.2 on 2019-05-01 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Masters',
            fields=[
                ('comp_id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('comp_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='dept',
            fields=[
                ('dept_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location_Masters',
            fields=[
                ('loc_id', models.IntegerField(max_length=2, primary_key=True, serialize=False)),
                ('loc_name', models.CharField(max_length=100)),
                ('comp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compliance.Company_Masters')),
            ],
        ),
        migrations.CreateModel(
            name='emplo',
            fields=[
                ('emp_id', models.IntegerField(max_length=6, primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compliance.dept')),
            ],
        ),
        migrations.AddField(
            model_name='dept',
            name='loc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compliance.Location_Masters'),
        ),
        migrations.CreateModel(
            name='Comp_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('reg_no', models.CharField(max_length=100)),
                ('license_type', models.CharField(max_length=200)),
                ('law_authority', models.CharField(blank=True, max_length=250, null=True)),
                ('date_purchase', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('date_expiry', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('renewal', models.CharField(blank=True, max_length=200, null=True)),
                ('present_fees', models.IntegerField(blank=True, max_length=20, null=True)),
                ('custody', models.CharField(max_length=20)),
                ('loc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compliance.Location_Masters')),
                ('primary_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Prim_emp', to='compliance.emplo')),
                ('sec_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secd_emp', to='compliance.emplo')),
            ],
        ),
    ]
