from django.contrib import admin
from django.urls import path

from qa.views import test

urlpatterns = [
    path('', test),
    path('login/', test),
    path('signup/', test),
    path('question/<int:id>/', test, name='test'),
    path('ask/', test),
    path('popular/', test),
    path('new/', test),
    path('admin/', admin.site.urls),
]
