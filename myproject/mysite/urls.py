from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import TopView
    
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', TopView.as_view(), name='top'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('allauth.urls')),
    path('testApp/', include('testApp.urls')),
]