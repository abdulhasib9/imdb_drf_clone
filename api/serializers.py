from rest_framework import serializers
from .models import Watchlist,StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta: 
        model =Review
        fields='__all__'



class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
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