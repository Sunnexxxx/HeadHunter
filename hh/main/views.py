from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

from .forms import VacancyCreateForm
from .models import User, Resume, Vacancy


class MainPage(TemplateView):
    template_name = 'start.html'


class Employer(TemplateView):
    template_name = 'employer.html'


class Applicaut(TemplateView):
    template_name = 'applicaut.html'


class Register(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('success')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        return super().get(request, *args, **kwargs)


class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    staf = None

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         if request.user.is_staff:
    #             self.staf = True
    #         else:
    #             self.staf = False
    #     print()
    #     print(self.staf)
    #     print()
    #     return super().get(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('employer')
        else:
            return reverse_lazy('applicaut')


class Logout(LogoutView):
    template_name = 'logout.html'
    next_page = reverse_lazy('main')
#
#
# def create_vacancy(request):
#     vacancy = Vacancy.objects.all()


class Detail(DetailView):
    model = Vacancy
    template_name = 'detail_page.html'
    slug_url_kwarg = 'vacancy_slug'
    extra_context = {
        'title': 'Detail'
    }


def create_view(request):
    form = VacancyCreateForm()
    context = {'form': form}
    if request.method == 'POST':
        form = VacancyCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            context['form'] = form

    return render(request, 'create_vacancy.html', context)
