from django.contrib import admin
from .models import Company, Vacancy, Specialty

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'logo', 'description', 'employee_count']

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'specialty', 'company', 'skills', 'description', 'salary_min', 'salary_max',
                    'published_at']

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'title', 'picture']

