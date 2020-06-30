# Generated by Django 3.0 on 2020-06-30 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('author_name', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
                'db_table': 'bz_author',
            },
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('press_name', models.CharField(max_length=128)),
                ('pic', models.ImageField(default='img/1.jpeg', upload_to='img')),
                ('address', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': '出版社',
                'verbose_name_plural': '出版社',
                'db_table': 'bz_press',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('book_name', models.CharField(max_length=128)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pic', models.ImageField(default='img/1.jpeg', upload_to='img')),
                ('authors', models.ManyToManyField(db_constraint=False, related_name='books', to='api.Author')),
                ('publish', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.Press')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
                'db_table': 'bz_book',
            },
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=11)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='api.Author')),
            ],
            options={
                'verbose_name': '作者详情',
                'verbose_name_plural': '作者详情',
                'db_table': 'bz_author_detail',
            },
        ),
    ]
