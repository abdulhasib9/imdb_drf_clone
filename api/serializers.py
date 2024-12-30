from rest_framework import serializers
from .models import Watchlist,StreamPlatform

class WatchlistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Watchlist
        fields ="__all__"
        

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchlistSerializer(many=True,read_only=True)
    
    # using the serializer specific fields 
    watchlist = serializers.StringRelatedField(many=True)
    class Meta:
        model = StreamPlatform
        fields ='__all__'