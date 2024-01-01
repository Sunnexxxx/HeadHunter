from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('employer/', Employer.as_view(), name='employer'),
    path('applicant/', Applicant.as_view(), name='applicant'),
    path('logout/', Logout.as_view(), name='logout'),
    path('create/', VacancyCreate.as_view(), name='create'),
    path('vacancy/', VacancyList.as_view(), name='vacancy'),
    path('vacancy/<int:pk>/', VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancy/<int:pk>/update/', VacancyUpdate.as_view(), name='vacancy_update'),
    path('vacancy/<int:pk>/delete/', VacancyDelete.as_view(), name='vacancy_delete'),
    path('vacancy_app/<int:pk>/', VacancyDetailApp.as_view(), name='vacancy_app'),
    path('applicant/create/', ResumeCreate.as_view(), name='resume_create'),
    path('applicant/<int:pk>/', ResumeDetail.as_view(), name='resume_detail'),
    path('applicant/<int:pk>/update/', ResumeUpdate.as_view(), name='resume_update'),
    path('employer/<int:pk>/', ResumeDetailEm.as_view(), name='resume_detail_em'),
]