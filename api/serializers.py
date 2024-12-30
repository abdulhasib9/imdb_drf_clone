from rest_framework.serializers import ModelSerializer
from .models import Watchlist,StreamPlatform

class WatchlistSerializer(ModelSerializer):
    class Meta:
        model =Watchlist
        fields ="__all__"
        

class StreamPlatformSerializer(ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields ='__all__'