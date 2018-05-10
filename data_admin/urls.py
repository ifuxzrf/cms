from django.urls import path
from data_admin import views

urlpatterns = [
    path('synonyms', views.SynonymsView.as_view(), name='synonyms'),
    path('emotional', views.EmotionalView.as_view(), name='emotional'),
    path('sensitive', views.SensitiveView.as_view(), name='sensitive'),
]
