from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('employer/', Employer.as_view(), name='employer'),
    path('applicaut/', Applicaut.as_view(), name='applicaut'),
    path('logout/', Logout.as_view(), name='logout'),
    path('create/', create_view, name='create'),
]