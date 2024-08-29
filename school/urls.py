from django.urls import path
from .views import (
    HomePageAPIView,
    AboutPageAPIView,
    TeacherPageAPIView,
)

urlpatterns = [
    path('homepage/', HomePageAPIView.as_view(), name='home-page-list'),
    path('aboutpage/',AboutPageAPIView.as_view(),name='about-page-view'),
    path('teacherpage/',TeacherPageAPIView.as_view(),name='teacher-page-view')
    
]