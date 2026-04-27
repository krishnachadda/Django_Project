from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('exam-form/', views.fill_exam_form, name='exam_form'),
    path('logout/', views.logout_view, name='logout'),
]