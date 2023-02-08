from django.contrib import admin
from django.urls import path

from qa.views import test

urlpatterns = [
    # path('/', ),
    # path('login/', ),
    # path('signup/', ),
    path('question/<int:id>/', test, name='test'),
    # path('ask/', ),
    # path('popular/', ),
    # path('new/', ),
    path('admin/', admin.site.urls),
]
