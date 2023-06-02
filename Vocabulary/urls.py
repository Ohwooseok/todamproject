from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
import Vocabulary

urlpatterns = [
    path('study', Vocabulary.views.study, name='study'),
    path('word', Vocabulary.views.word, name='word'),
    path('test', Vocabulary.views.test, name='test'),
    path('vocabulary', Vocabulary.views.vocabulary, name='vocabulary'),
]

