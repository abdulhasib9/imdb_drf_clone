from rest_framework.serializers import ModelSerializer
from .models import Watchlist,StreamPlatform

class WatchlistSerializer(ModelSerializer):
    
    class Meta:
        model =Watchlist
        fields ="__all__"
        

class StreamPlatformSerializer(ModelSerializer):
    watchlist = WatchlistSerializer(many=True,read_only=True)
    class Meta:
        model = StreamPlatform
        fields ='__all__'