from django.urls import path
from .views import home, createShortenURLView, redirectView

app_name = "url"

urlpatterns = [
    path('', home, name='home'),
    path('create/', createShortenURLView, name='create'),
    path('<str:url>', redirectView, name='redirect')
]