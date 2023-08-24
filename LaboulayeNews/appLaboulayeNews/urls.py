from django.urls import path, re_path
from . import views

urlpatterns = [
    path('<int:current_page>/', views.home, name = 'home'),
    path('category/<str:cat>/<int:current_page>/', views.category, name="categories"),
    path('news/<int:id>/', views.news, name='news'),
    re_path(r'^.*$', views.home, name='home'),
    ]