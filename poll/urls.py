from django.urls import path

from poll import views

urlpatterns = [
    path('poll/load_form', views.load_form),
    path('edit/<int:id>', views.edit, name='edit')

]