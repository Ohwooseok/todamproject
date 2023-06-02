from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
import Vocabulary

urlpatterns = [
    path('study', Vocabulary.views.study, name='study'),
    path('word', Vocabulary.views.word, name='word'),
    path('vocabulary', Vocabulary.views.vocabulary, name='vocabulary'),
]

