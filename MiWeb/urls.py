from django import views
from django.contrib import admin
from django.urls import path
from AppFamilia.views import familia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/',familia),
]
