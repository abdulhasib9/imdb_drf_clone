from . import views 
from django.urls import path


urlpatterns = [
    path('watchlist/',views.WatchlistAV.as_view()),
    path('movie/<int:pk>/',views.WatchlistDetailAV.as_view()),
    path('platforms/',views.StreamPlatformAV.as_view())
]
