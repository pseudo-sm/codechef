
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('compile/',views.compile,name="compile"),
    path('start-exam/',views.start_exam),
    path('start-exam2/',views.start_exam2),
    path('start-exam3/',views.start_exam3),
    path('compile/',views.compile,name="compile"),
    path('submit/',views.submit1,name="submit"),
    path('submit2/',views.submit2,name="submit2"),
    path('submit3/',views.submit3,name="submit3"),
    path('desert/', views.editor3,name="editor3"),
    path('main/', views.editor2,name="editor2"),
    path('', views.editor,name="editor"),


]
