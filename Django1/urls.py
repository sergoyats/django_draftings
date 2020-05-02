"""Django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app_1.views import gen_password, filter_by_state_city, counting_unique_firstnames, get_turnover, list_of_orders


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gen_password/', gen_password),
    path('filter_by_state_city/', filter_by_state_city),
    path('counting_unique_firstnames/', counting_unique_firstnames),
    path('get_turnover/', get_turnover),
    path('list_of_orders/', list_of_orders),
    path('', admin.site.urls)
]
