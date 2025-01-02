from . import views 
from django.urls import path


urlpatterns = [
    path('watchlist/',views.WatchlistAV.as_view()),
    path('movie/<int:pk>/',views.WatchlistDetailAV.as_view()),
    path('platforms/',views.StreamPlatformAV.as_view()),
    path('platform/<int:pk>/',views.StreamPlatformDetailAV.as_view()),
    path('movie/<int:pk>/review-create/',views.ReviewCreate.as_view()),
    path('movie/<int:pk>/reviews/',views.ReviewList.as_view()),
    path('review/<int:pk>/',views.ReviewDetail.as_view()),
    path('review-list/',views.ReviewList.as_view())
    
]
