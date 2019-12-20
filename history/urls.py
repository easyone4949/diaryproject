from django.urls import path
from . import views


urlpatterns = [
    path('history/', views.history, name="history"),
]
#이렇게 해야 업로드된 파일을 읽을 수 있음