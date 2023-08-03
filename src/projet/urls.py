from django.urls import path
from .views import index, working_days_view

urlpatterns = [
    path('', index, name="projet-index"),
    path('working_days/<int:year>/', working_days_view, name='working_days_view'),
]