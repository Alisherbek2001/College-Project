from django.urls import path
from .views import (
    HomePageAPIView,
    AboutPageAPIView,
    TeacherPageAPIView,
    BlogPageAPIView,
)

urlpatterns = [
    path('homepage/', HomePageAPIView.as_view(), name='home-page-list'),
    path('aboutpage/',AboutPageAPIView.as_view(),name='about-page-view'),
    path('teacherpage/',TeacherPageAPIView.as_view(),name='teacher-page-view'),
    path('blogpage/',BlogPageAPIView.as_view(),name='blog-pagelist'),
    
]