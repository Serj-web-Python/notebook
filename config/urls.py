"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path,include

# --- НАСТРОЙКИ АДМИНКИ ---
# 1. Текст в шапке (вместо Django administration)
admin.site.site_header = "Управление Блокнотом"

# 2. Текст во вкладке браузера (Title)
admin.site.site_title = "Панель администратора"

# 3. Текст на главной странице админки (над списком моделей)
admin.site.index_title = "Добро пожаловать, Шеф!"


urlpatterns = [
    path('manager-panel/', admin.site.urls),
    path('', include('blocnot.urls')),

    path('accounts/', include('django.contrib.auth.urls')),  #Эта одна строчка автоматически подключает готовые пути Django: /login/, /logout/, /password_change/ и т.д.
                        #Нам нужно было только создать шаблоны (мы создали login.html).
]
