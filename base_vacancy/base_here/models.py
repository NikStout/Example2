from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=24, default='Компания')
    location = models.CharField(max_length=16, default='Москва')
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField(default='Информация')
    employee_count = models.IntegerField(null=True)


class Specialty(models.Model):
    code = models.CharField(max_length=24, default='backend')
    title = models.CharField(max_length=24, default='Бэкэнд')
    picture = models.URLField(default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    title = models.CharField(max_length=64, default='Джуниор')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies', default='2')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies', default='2')
    skills = models.TextField(blank=True)
    description = models.TextField(default='Описание')
    salary_min = models.IntegerField(null=True)
    salary_max = models.IntegerField(null=True)
    published_at = models.DateField(auto_now=True)
