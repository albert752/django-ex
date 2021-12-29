from django.conf import settings
from django.urls import path
from django.contrib import admin

from welcome.views import index, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('', index),
    path('health/', health),
    path('admin/', admin.site.urls),
]

