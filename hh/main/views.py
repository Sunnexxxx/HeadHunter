from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, DetailView, ListView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import VacancyForm, ResumeForm
from .models import User, Resume, Vacancy
from django.contrib.auth import login
from django.views.generic.edit import FormView, UpdateView, DeleteView
from .forms import CustomUserCreationForm


class MainPage(TemplateView):
    template_name = 'start.html'


class Register(FormView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = form.cleaned_data['is_staff']
        user.save()

        login(self.request, user)

        if user.is_staff:
            return redirect('employer')
        else:
            return redirect('applicant')


class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    staf = None

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('employer')
        else:
            return reverse_lazy('applicant')


class Logout(LogoutView):
    next_page = reverse_lazy('main')


class Employer(TemplateView):
    template_name = 'employer/employer.html'


class VacancyCreate(CreateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'employer/create_vacancy.html'
    success_url = reverse_lazy('employer')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VacancyList(ListView):
    model = Vacancy
    template_name = 'employer/vacancy_list.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.filter(user=self.request.user)


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'employer/vacancy_detail.html'
    context_object_name = 'vacancy'


class VacancyUpdate(UpdateView):
    model = Vacancy
    template_name = 'employer/vacancy_update.html'
    fields = ['name', 'company', 'salary', 'skills', 'duty', 'email']
    success_url = reverse_lazy('vacancy')


class VacancyDelete(DeleteView):
    model = Vacancy
    template_name = 'employer/vacancy_delete.html'
    success_url = reverse_lazy('vacancy')


class Applicant(ListView):
    model = Vacancy
    template_name = 'applicant/applicant.html'
    context_object_name = 'vacancies'


class VacancyDetailApp(DetailView):
    model = Vacancy
    template_name = 'applicant/vacancy_detail_applicant.html'
    context_object_name = 'vacancy'


class ResumeList(ListView):
    model = Resume
    template_name = 'employer/employer.html'
    context_object_name = 'resumes'


class ResumeCreate(View):
    template_name = 'applicant/resume_create.html'

    def get(self, request):
        existing_resume = Resume.objects.filter(user=request.user).first()

        if existing_resume:
            return redirect('resume_update', pk=existing_resume.pk)

        form = ResumeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        existing_resume = Resume.objects.filter(user=request.user).first()

        if existing_resume:
            return redirect('resume_update', pk=existing_resume.pk)

        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_detail', pk=resume.pk)

        return render(request, self.template_name, {'form': form})


class ResumeDetail(View):
    template_name = 'applicant/resume_detail.html'

    def get(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk, user=request.user)
        return render(request, self.template_name, {'resume': resume})


class ResumeUpdate(View):
    template_name = 'applicant/resume_update.html'

    def get(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk, user=request.user)
        form = ResumeForm(instance=resume)
        return render(request, self.template_name, {'form': form, 'resume': resume})

    def post(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk, user=request.user)
        form = ResumeForm(request.POST, instance=resume)

        if form.is_valid():
            form.save()
            return redirect('resume_detail', pk=pk)

        return render(request, self.template_name, {'form': form, 'resume': resume})







