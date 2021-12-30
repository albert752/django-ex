from django.conf import settings
from django.urls import path
from django.contrib import admin

from welcome.views import index, health
from api.views import GetAllItems, GetItem


urlpatterns = [
    path('', index),
    path('health/', health),
    path('admin/', admin.site.urls),
    path('items/', GetAllItems.as_view()),
    path('item/', GetItem.as_view())
]

