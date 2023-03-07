from django.contrib import admin
from django.urls import path

from qa.views import get_new_questions, get_popular_questions, question_detail, ask_question, user_signup, user_login

urlpatterns = [
    path('', get_new_questions, name='new_questions'),
    path('popular/', get_popular_questions, name='popular_questions'),
    path('question/<int:pk>/', question_detail, name='detail_question'),
    path('login/', user_login, name='user_login'),
    path('signup/', user_signup, name='user_signup'),
    path('ask/', ask_question, name='ask_question'),
    # path('new/', test),
    path('admin/', admin.site.urls),
]
