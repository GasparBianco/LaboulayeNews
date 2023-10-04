from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('<int:current_page>/', views.home, name = 'home'),
    path('', views.home, name = 'home'),
    path('category/<str:cat>/<int:current_page>/', views.category, name="categories"),
    path('news/<int:id>/', views.news, name='news'),
    path('contact/', views.contact, name='contact')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)