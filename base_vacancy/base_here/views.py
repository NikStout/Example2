from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views.generic import ListView, DetailView, TemplateView
from .models import Vacancy, Specialty, Company


class main_view(TemplateView):
    template_name = 'base_here/index.html'

    def get_context_data(self, **kwargs):
        context = super(main_view, self).get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.all()
        context['companies'] = Company.objects.all()
        return context


class Vacancies_specialtiesView(ListView):
    model = Vacancy
    template_name = 'base_here/vacancies.html'
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['vacancies']:
            context['title'] = 'Вакансии для ' + str(context['vacancies'][0].specialty.title)
        else:
            context['title'] = 'Вакансии не найдены'
        return context

    def get_queryset(self):
        return Vacancy.objects.filter(specialty_id__code=self.kwargs['specialty'])


class AllVacanciesView(ListView):
    model = Vacancy
    template_name = 'base_here/vacancies.html'
    context_object_name = 'vacancies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'все вакансии'
        return context

    def get_queryset(self):
        return Vacancy.objects.all()


class CompanyView(ListView):
    model = Vacancy
    template_name = 'base_here/company.html'
    context_object_name = 'vacancies'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_name'] = str(context['vacancies'][0].company.name)
        context['location'] = str(context['vacancies'][0].company.name)
        return context

    def get_queryset(self):
        return Vacancy.objects.filter(company_id=self.kwargs['id'])


class VacancyView(DetailView):
    model = Vacancy
    template_name = 'base_here/vacancy.html'
    pk_url_kwarg = 'id'
    context_object_name = 'vacancy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страницы не существует!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
