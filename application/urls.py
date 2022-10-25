from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('result', views.viewresult, name='result'),
    path('result2', views.viewresult2, name='result2')
]
