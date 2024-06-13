from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view, name='home'),
    path('submit-answer/', views.submit_answer, name='submit_answer'),
    path('get-question/<int:level>/', views.get_question, name='get_question'),
]
