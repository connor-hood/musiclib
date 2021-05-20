from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:pk>/', views.SongDetail.as_view()),
    path('', RedirectView.as_view(url='/music/')),
]
