
from django.contrib import admin
from django.urls import path
from Testapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('hobbie/', Hobbie_page),
    path('pet/', Pet_page),
    path('font/',Font_page)
]


