from django.urls import path
from . import views
urlpatterns = [
    path('wdowinsurance/', views.wdowinsurance),
    path('wdowinsurance/get_started/', views.get_started),
]
