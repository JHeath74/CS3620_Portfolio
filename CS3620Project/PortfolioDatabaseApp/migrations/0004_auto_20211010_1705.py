# Generated by Django 2.2 on 2021-10-10 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabaseApp', '0003_auto_20211009_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HobbyName', models.CharField(max_length=200)),
                ('HobbyDescription', models.CharField(max_length=200)),
                ('HobbyImage', models.CharField(default='https://media.istockphoto.com/vectors/outline-colorful-doodle-hobbies-set-stay-home-concept-top-table-and-vector-id1222703360?s=612x612', max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='MyHobbys',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='PortfolioImage',
            field=models.CharField(default='https://centralaz.edu/wp-content/uploads/2017/08/CIS_Comp_Prog_Main_507378942.jpg', max_length=500),
        ),
    ]
