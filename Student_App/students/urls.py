from django.urls import path
from .views import *

urlpatterns=[
    path('reg',RegView.as_view(),name='reg'),
    path('home',LandingView.as_view(),name='home'),
    path('students',StudentView.as_view(),name='students'),
    path('add',AddStudentsView.as_view(),name='add'),
    path('delete/<int:id>',DeleteStudentView.as_view(),name='delete'),
    path('edit/<int:id>',EditStudentView.as_view(),name='edit'),
    path('logout/', LogoutView.as_view(), name='logout')
    
]