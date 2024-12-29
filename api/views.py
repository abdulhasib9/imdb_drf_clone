from django.shortcuts import render
from rest_framework.response import Response
from .models import Watchlist,StreamPlatform
from rest_framework.views import APIView

class WatchlistAV(APIView):
    def get(self,request):
        watchlists = Watchlist.objects.all()
        data = list(watchlists.values())
        return Response(data)
