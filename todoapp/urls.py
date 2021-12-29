from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('in_process/<list_id>', views.in_process, name='in_process'),
    path('done/<list_id>', views.done, name='done'),
    path('edit/<list_id>', views.edit, name='edit'),
]
