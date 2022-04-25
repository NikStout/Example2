from django.urls import path
import base_here.views as views

urlpatterns = [
    path('', views.main_view.as_view(), name='main'),
    path('vacancies/cat/<str:specialty>/', views.Vacancies_specialtiesView.as_view(), name='Vacancies_specialtiesView'),
    path('vacancies/', views.AllVacanciesView.as_view(), name='AllVacanciesView'),
    path('companies/<int:id>/', views.CompanyView.as_view(), name='CompanyView'),
    path('vacancies/<int:id>/', views.VacancyView.as_view(), name='VacancyView'),

]
