from django.conf.urls import url,include
from .views import *

from django.urls import path

urlpatterns = [
    path(r'^cord/$', cord_nat),
]