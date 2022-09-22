from django.urls import path

from .views import IndexView

urlpatterns = [
    path('restrito', IndexView.as_view(), name='index'),
]
