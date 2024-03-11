
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('new_feedback/', views.new_feedback, name='new_feedback'),
    path('my_feedbacks/', views.my_feedbacks, name='my_feedbacks'),
]
